'''
Created on Sep 24, 2011

@author: jianhuashao
'''
from django.shortcuts import render_to_response, HttpResponse
from django.http import HttpResponseRedirect
import datetime

def hello(request):
    return HttpResponse("Hello Wrold")

def current_datetime(request):
    now = datetime.datetime.now()
    assert False
    html = "<html><body>it is now %s. </body></html>" % now
    return HttpResponse(html)

def welcome(request):
    return render_to_response('welcome.html')

def welcome_request(request):
    if request.method == 'POST':
        if request.POST.get('view_borrow'):
            return HttpResponseRedirect('/book/')
        if request.POST.get('books_donation'):
            return HttpResponseRedirect('/book/donation')
        if request.POST.get('admin'):
            return HttpResponseRedirect('/admin/')