# Create your views here.
from django.shortcuts import render_to_response, HttpResponse
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.core.mail import send_mail, EmailMessage
from models import *
from myutil import borrow_status_string 

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


def book_donation_context(book_donation):
    #donaters = book_donation.donater.all()
    #donaters_html = ""
    #for donater in donaters:
    #    donaters_html += donater.first_name+" "+donater.last_name+", "
    donaters_html = book_donation.donater
    book_context = {
        "donater": donaters_html,
        "donate_date": book_donation.donate_date,
        }
    return book_context

def book_borrow_record(borrow_record, status_string):
    status = Borrow_status.objects.get(status=status_string)
    borrow_status = borrow_record.borrow_status
    if (borrow_status == status):
        return True
    else:
        return False

#def borrow_record_check(borrow_record, status):
#    borrow_status = book_borrow_record(borrow_record, status)
#    if (borrow_status == True):


def borrow_record_context(book):
    borrows = []
    borrow_records = book.borrow_record_set.all()
    for borrow_record in borrow_records:
        borrow_status = book_borrow_record(borrow_record, borrow_status_string.WAITING_FOR_RETURN)
        #borrow_status = True
        if (borrow_status == True):
            borrow = {
                "borrower":borrow_record.borrower,
                "from":borrow_record.borrow_date,
                "to":borrow_record.return_date,
                "status":borrow_record.borrow_status,
                }
            borrows.append(borrow)
    return borrows
            

def book_borrowed_count(book):
    book_borrowed = 0
    borrow_records = book.borrow_record_set.all()
    for borrow_record in borrow_records:
        borrow_status = book_borrow_record(borrow_record, borrow_status_string.WAITING_FOR_RETURN)
        if (borrow_status == True):
            book_borrowed += 1
    return book_borrowed


def book_context(book):
    #authors = book.author.all()
    #author_html = ""
    #for author in authors:
    #    author_html += author.first_name+" "+author.last_name+", "
    author_html = book.author
    # book donaters 
    book_donations_c = []
    book_donations = book.book_donation_set.all()
    book_total = len(book_donations)
    for book_donation in book_donations:
        book_donation_c = book_donation_context(book_donation)
        book_donations_c.append(book_donation_c)
    book_borrowed = book_borrowed_count(book)
    book_available = book_total - book_borrowed
    if (book_available > 0):
        book_availability  = True
    else:
        book_availability = False
    book_context = {
        "id": book.id,
        "title": book.title,
        "publisher": book.publisher.name,
        "publication_date": book.publication_date,
        "authors":author_html,
        "donaters":book_donations_c, 
        "availability": book_availability
        }
    return book_context

def display_books(request):
    books_c = []
    books = Book.objects.all()
    for book in books:
        book_c = book_context(book)
        books_c.append(book_c)
    context = {"books":books_c}
    return render_to_response('book_list.html', context)
    #return HttpResponse("hello")

def display_book_by_id(request, book_id):
    book = Book.objects.get(id=book_id)
    book_c = book_context(book)
    book_donations_c = []
    book_donations = book.book_donation_set.all()
    for book_donation in book_donations:
        book_donation_c = book_donation_context(book_donation)
        book_donations_c.append(book_donation_c)
    borrow_record_c = borrow_record_context(book)
    context = {"book":book_c, "book_donation":book_donations_c, 'borrows':borrow_record_c}
    return render_to_response('book_detail.html', context)
    #return render_to_response("borrow_form.html")

def borrow_book_by_id(request, book_id):
    book = Book.objects.get(id=book_id)
    book_c = book_context(book)
    errors = []
    if request.method == 'POST':
        if request.POST.get('email') and '@' not in request.POST['email']:
            errors.append('Enter a valid e-mail address.')
        if not request.POST.get('first_name', ''):
            errors.append('Enter a first name.')
        if not request.POST.get('last_name', ''):
            errors.append('Enter a last name.')
        if not request.POST.get('telephone', ''):
            errors.append('Enter a contact No..')
        if not request.POST.get('subjects', ''):
            errors.append('Enter a study subject.')
        if not request.POST.get('study_period_from', ''):
            errors.append('Enter when you start your study.')
        if not request.POST.get('study_period_to', ''):
            errors.append('Enter when you will finish your study.')
        if not request.POST.get('address', ''):
            errors.append('Enter your current address.')
        if not errors:
            send_mail(
                "You are requesting to borrow a copy of <"+book.title+">",
                request.POST['address'],
                "jianwen@nottingham.ac.uk",
                [request.POST.get('email')],
            )
            return HttpResponseRedirect('/book/'+str(book.id)+'/borrow/request_result/')
    borrower_c = {
        "email": request.POST.get('email', ''),
        "first_name": request.POST.get('first_name', ''),
        "last_name": request.POST.get('last_name', ''),
        "telephone": request.POST.get('telephone', ''),
        "subjects": request.POST.get('subjects', ''),
        "study_period_from": request.POST.get('study_period_from', ''),
        "study_period_to": request.POST.get('study_period_to', ''),
        "address": request.POST.get('address', ''),
        }
    context = {"book":book_c, "errors":errors, "borrower":borrower_c}
    return render_to_response('borrow_form.html', context, context_instance = RequestContext(request))
    
    
def borrow_result_by_id(request, book_id):
    return HttpResponse('Thanks')
    

def book_borrow(request, book_id):
    errors = []
    if request.method == 'POST':
        if not request.POST.get('subject', ''):
            errors.append('Enter a subject.')
        if not request.POST.get('message', ''):
            errors.append('Enter a message.')
        if request.POST.get('email') and '@' not in request.POST['email']:
            errors.append('Enter a valid e-mail address.')
        if not errors:
            send_mail(
                request.POST['subject'],
                request.POST['message'],
                request.POST.get('email', 'noreply@example.com'),
                ['siteowner@example.com'],
            )
            return HttpResponseRedirect('/contact/thanks/')
    return render_to_response('contact_form.html', {
        'errors': errors,
        'subject': request.POST.get('subject', ''),
        'message': request.POST.get('message', ''),
        'email': request.POST.get('email', ''),
    })
    

   
def donation_request(request):
    errors = []
    if request.method == 'POST':
        if request.POST.get('email') and '@' not in request.POST['email']:
            errors.append('Enter a valid e-mail address.')
        if not request.POST.get('name', ''):
            errors.append('Enter your name.')
        if not request.POST.get('telephone', ''):
            errors.append('Enter a contact No..')
        if not request.POST.get('books', ''):
            errors.append('Enter book titles.')
        if not errors:
            donation_request_object = Book_donation_request(
                donater_email=request.POST.get('email'),
                donater_telephone=request.POST.get('telephone', ''),
                donater_name=request.POST.get('name', ''),
                donater_books=request.POST.get('books', ''),
                donater_message=request.POST.get('message', ''),
                )
            donation_request_object.save()
            email = EmailMessage(
                subject="Thanks very much for your book donation",
                body=
                    "You just recently donate books with title ("+
                    request.POST.get('books', '')+"). "+
                    "Library volunteers will contact you soon to collect books. "+
                    "\nThanks very much "+
                    "\nJianWenLibrary",
                from_email='wenwen.bao1203@gmail.com',
                to=[request.POST.get('email')],
                )
            email.send()
            email = EmailMessage(
                subject="JianWenLibrary: One new donation",
                body=
                    "books: "+request.POST.get('books', '')+"\n"+
                    "telephone: "+request.POST.get('telephone', '')+"\n"+
                    "name: "+request.POST.get('name', '')+"\n"+
                    "email: "+request.POST.get('email', '')+"\n"+
                    "message: "+request.POST.get('message', '')+"\n",
                from_email=request.POST.get('email'),
                to=['dustin.shaojianhua@gmail.com', "jianhua.shao1986@gmail.com"],
                )
            email.send()
            return HttpResponseRedirect('/book/donation_result/')
    donater_c = {
        "email": request.POST.get('email', ''),
        "name": request.POST.get('name', ''),
        "telephone": request.POST.get('telephone', ''),
        "telephone": request.POST.get('telephone', ''),
        "books": request.POST.get('books', ''),
        "message": request.POST.get('message', ''),
        }
    context = {"errors":errors, "borrower":donater_c}
    return render_to_response('donation_request_form.html', context, context_instance = RequestContext(request))


def donation_result(request):
    return render_to_response('donation_result.html')