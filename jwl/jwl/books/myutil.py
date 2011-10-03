'''
Created on Sep 25, 2011

@author: jianhuashao
'''

class borrow_status_string:
    WAITING_FOR_BORROW = "Waiting for Borrow"
    WAITING_FOR_CONFIRM = "Waiting for email confirm"
    WAITING_FOR_RETURN = "Waiting for return"
    RETURNED = "Returned"
    
    
class donation_status_string:
    REQUEST_TO_DONATE = "Request for donation"
    ACCEPT_DONATION_REQUEST = "Accept donation request"
    RECEIVED_BOOK_INTO_LIBRARY = "Received book and saved in library"