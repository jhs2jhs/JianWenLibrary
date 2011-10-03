from django.db import models

# Create your models here.
class Publisher (models.Model):
    name = models.CharField(max_length=30)
    def __unicode__(self):
        return self.name
    

class Author (models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=40) 
    def __unicode__(self):
        return self.first_name+" "+self.last_name
    
# if not study in nottingham, it should be "never studied in university"    
class Study_subject (models.Model):
    subject = models.CharField(max_length=100)
    def __unicode__(self):
        return self.subject
    

class Book_donater(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=40)
    email = models.EmailField()
    telephone = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    subjects = models.ForeignKey(Study_subject)
    study_period_from = models.DateField(blank=True, null=True)
    study_period_to = models.DateField(blank=True, null=True)
    def __unicode__(self):
        return self.first_name+" "+self.last_name
    
    
class Book (models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author)
    publisher = models.ForeignKey(Publisher)
    publication_date = models.DateField()
    default_availability = models.BooleanField()
    selling_price = models.DecimalField(max_digits=5, decimal_places=2)
    def __unicode__(self):
        return self.title
 
class Book_donation_request(models.Model):
    donater_email = models.CharField(max_length=100)
    donater_telephone = models.CharField(max_length=100)
    donater_name = models.CharField(max_length=100)
    donater_books = models.CharField(max_length=100)
    donater_message = models.CharField(max_length=200)
    request_process = models.BooleanField()
    def __unicode__(self):
        return r''+self.donater_email

class Book_donation_status(models.Model):
    donation_status = models.CharField(max_length=30)
    def __unicode__(self):
        return r''+self.status
    
    
class Book_donation(models.Model):
    book = models.ForeignKey(Book)
    donater = models.ForeignKey(Book_donater)
    donate_date = models.DateField()
    donate_status = models.ForeignKey(Book_donation_status)
    def __unicode__(self):
        return "self.donater"
    
 # can use to check how many copies left for a specific book, however, a person can only booked for one person   
class Book_copies(models.Model):
    book = models.ForeignKey(Book)
    copies = models.IntegerField()
    def __unicode__(self):
        return u''+self.copies
    
    
# the email address must be end with "@nottingham.ac.uk" or "@nottingham.edu.cn"
class Borrower(models.Model):
    email = models.EmailField()
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=40) 
    telephone = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    subjects = models.ForeignKey(Study_subject)
    study_period_from = models.DateField(blank=True, null=True)
    study_period_to = models.DateField(blank=True, null=True)
    def __unicode__(self):
        return self.first_name+" "+self.last_name


# need to put it into a seperate files.    
class Borrow_status (models.Model):
    status = models.CharField(max_length=100)
    def __unicode__(self):
        return u''+self.status
        
    
class Borrow_record(models.Model):
    book = models.ForeignKey(Book)
    borrower= models.ForeignKey(Borrower)
    confirm_string = models.CharField(max_length=100)
    borrow_date = models.DateField()
    return_date = models.DateField()
    borrow_status = models.ForeignKey(Borrow_status)
    def __unicode__(self):
        return self.confirm_string    
