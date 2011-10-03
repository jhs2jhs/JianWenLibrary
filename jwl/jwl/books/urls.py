'''
Created on Sep 25, 2011

@author: jianhuashao
'''
from django.conf.urls.defaults import patterns, include, url
from django.views.generic.simple import direct_to_template
from django.views.generic import list_detail

urlpatterns = patterns('books.views',
    url('^test/$', 'test'),
    url('^test/mail$', 'test_mail'),
    url('^$', 'display_books'),
    url('^(?P<book_id>\d*)/$', 'display_book_by_id'),
    url('^(?P<book_id>\d*)/borrow/$', 'borrow_book_by_id'),
    url('^(?P<book_id>\d*)/borrow/request_result$', 'borrow_result_by_id'),
)

