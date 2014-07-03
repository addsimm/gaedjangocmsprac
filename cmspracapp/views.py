# Create your views here.

from django.http import HttpResponse
from django import template
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
import datetime

def home(request):
    now = datetime.datetime.now()
    return render_to_response('home.html',
                              {'now': now,}
    )