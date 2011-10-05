'''
Created on Sep 25, 2011

@author: jianhuashao
'''
from django.contrib import admin
#from jwl.books.models import *
from books.models import *

class PublisherAdmin(admin.ModelAdmin):
    list_display = ('name', )

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name')
    search_fields = ('first_name', 'last_name')

class StudySubjectAdmin(admin.ModelAdmin):
    list_display = ('subject', )

class BookDonaterAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'telephone', 'address')

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'publisher', 'publication_date', 'default_availability', 'selling_price', 'url')

class BookDonationRequestAdmin(admin.ModelAdmin):
    list_display = ('donater_email', 'donater_telephone', 'donater_name', 'donater_books', 'donater_message', 'request_process')

class BookDonationStatusAdmin(admin.ModelAdmin):
    list_display = ('donation_status', )

class BookDonationAdmin(admin.ModelAdmin):
    list_display = ('book', 'donater', 'donate_date', 'donate_status')
    
class BookCopiesAdmin(admin.ModelAdmin):
    list_display = ('book', 'copies')
    
class BorrowerAdmin(admin.ModelAdmin):
    list_display = ('email', 'first_name', 'last_name', 'telephone', 'address')

class BorrowStatusAdmin(admin.ModelAdmin):
    list_display = ('status', )

class BorrowRecordAdmin(admin.ModelAdmin):
    list_display = ('book', 'borrower', 'confirm_string', 'borrow_date', 'return_date', 'borrow_status')
    list_filter = ('book', )


admin.site.register(Publisher, PublisherAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Study_subject, StudySubjectAdmin)
admin.site.register(Book_donater, BookDonaterAdmin)
admin.site.register(Book, BookAdmin)
admin.site.register(Book_donation_request, BookDonationRequestAdmin)
admin.site.register(Book_donation_status, BookDonationStatusAdmin)
admin.site.register(Book_donation, BookDonationAdmin)
admin.site.register(Book_copies, BookCopiesAdmin)
admin.site.register(Borrower, BorrowerAdmin)
admin.site.register(Borrow_status, BorrowStatusAdmin)
admin.site.register(Borrow_record, BorrowRecordAdmin)
