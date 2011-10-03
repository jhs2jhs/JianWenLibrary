# Create your views here.
from django.shortcuts import render_to_response, HttpResponse
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.core.context_processors import csrf
from django.template import RequestContext
from django.core.mail import send_mail, EmailMessage
import smtplib

def display_meta(request):
    values = request.META.items()
    values.sort()
    html = []
    for k, v in values:
        html.append('<tr><td>%s</td><td>%s</td></tr>' % (k, v))
    return HttpResponse('<table>%s</table>' % '\n'.join(html))


def test(request):
    return HttpResponse('hello')

def test_mail(request):
    send_mail('Subject here', 'Here is the message.', 'psxjs4@nottingham.ac.uk',
    ['jianhua.shao1986@gmail.com'], fail_silently=False)
    #email = EmailMessage('Hello', 'World', to=['dustin.shaojianhua@gmail.com'])
    #email.send()
    return HttpResponse('hello email')