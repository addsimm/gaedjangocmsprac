# Create your views here.

import datetime
from socket import gethostname
import urllib2

from django.shortcuts import render_to_response, redirect
from django.views.decorators.csrf import csrf_exempt
from google.appengine.api import users

from gaedjangocmsprac.models import *


def return_template_values(path):
    if users.get_current_user():
        url = users.create_logout_url(path)
        url_linktext = 'sign out'
        template_values = {'user': users.get_current_user().nickname()}
    else:
        url = users.create_login_url(path)
        url_linktext = 'sign in'
        template_values = {}

    now = datetime.datetime.now()
    host = gethostname()
    template_values.update({'url': url,
                            'url_linktext': url_linktext,
                            'now': now,
                            'host': host,
                            'path': path
    })

    return template_values


def home(request):
    path = request.get_full_path()
    page_name = 'Home'
    print(request.get_host())
    search_string = ''
    flatpages_key_query = Flatpage.query(ancestor=flatpages_key())
    flatpages_keys = flatpages_key_query.fetch(20, keys_only=True)

    if 'q' in request.GET and (request.GET['q'] != 'search' or request.GET['q'] != ''):
        search_string = request.GET['q']
        flatpages = ndb.get_multi(flatpages_keys)
        flatpages_keys = []
        for flatpage in flatpages:
            if search_string.lower() in flatpage.fp_content.lower():
                flatpages.remove(flatpage)
                flatpages_keys.append(flatpage.key)

    template_values = return_template_values(path)
    template_values.update({'page_name': page_name,
                            'search_string': search_string,
                            'flatpages_keys': flatpages_keys,
    })
    return render_to_response('home.html', template_values)


@csrf_exempt
def create_flatpage(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        print('title: ', title)
        if title == u'':
            title = 'Untitled'
        print('title2: ', title)
        flatpage = Flatpage.get_or_insert(title, parent=flatpages_key())  # finicky about order of args in get or insert
        flatpage.fp_author = request.POST.get('author')
        flatpage.fp_content = request.POST.get('content')
        flatpage.put()
        return redirect('home')

    if request.method == 'GET':
        path = request.get_full_path()
        page_name = 'Create Flatpage'
        template_values = return_template_values(path)
        template_values.update({'page_name': page_name})
        return render_to_response('create_flatpage.html', template_values)


def display_flatpage(request):
    query_string = request.META['QUERY_STRING']
    query_string = urllib2.unquote(query_string)
    flatpage = Flatpage.get_by_id(parent=flatpages_key(), id=query_string)
    title = flatpage.key.string_id()                                                       # can change to query_string
    path = request.get_full_path()
    template_values = return_template_values(path)
    template_values.update({'page_name': title,
                            'flatpage': flatpage,
    })
    return render_to_response('flatpage.html', template_values)
