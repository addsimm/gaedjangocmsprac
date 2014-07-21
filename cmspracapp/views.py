# Create your views here.

import datetime
from socket import gethostname

from django.shortcuts import render_to_response
from google.appengine.api import users


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
    template_values = return_template_values(path)
    template_values.update({'page_name': page_name})
    return render_to_response('home.html', template_values)


def create_flatpage(request):
    return render_to_response('create_flatpage.html')