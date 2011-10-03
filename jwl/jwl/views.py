'''
Created on Sep 24, 2011

@author: jianhuashao
'''

from django.http import HttpResponse
import datetime

def hello(request):
    return HttpResponse("Hello Wrold")

def current_datetime(request):
    now = datetime.datetime.now()
    assert False
    html = "<html><body>it is now %s. </body></html>" % now
    return HttpResponse(html)
