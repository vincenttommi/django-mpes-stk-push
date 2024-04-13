from django.shortcuts import render
from django.http import HttpResponse
from django_daraja.mpesa.core import MpesaClient

def index(request):
    c1 = MpesaClient()
    # Use a Safaricom number that you have access to in order to get a prompt
    phone_number = '0759209325'
    amount = 1
    account_reference = 'reference'
    transaction_desc = 'Description'
    callback_url = 'https://darajambili.herokuapp.com/express-payment'
    response = c1.stk_push(phone_number, amount, account_reference, transaction_desc, callback_url)
    return HttpResponse(response)

def stk_push_callback(request):
    data = request.body
    return HttpResponse("STK Push in Django")


   

# def index(request):
#         cl = MpesaClient()
#         phone_number = '0700111222'
#         amount = 1
#         transaction_desc = 'Business Payment Description'
#         occassion = 'Test business payment occassion'
#         callback_url = 'https://api.darajambili.com/b2c/result'
#         response = cl.business_payment(phone_number, amount, transaction_desc, callback_url, occassion)
#         return HttpResponse(response)

