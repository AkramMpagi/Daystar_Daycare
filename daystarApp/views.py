from django.shortcuts import render
from daystarApp import views
from django.http import HttpResponse, HttpResponseRedirect
from . import urls
from .models import *
from .forms import *
from django.urls import reverse

# Create your views here.
def index(request):
    return render(request, 'daystarApp/index.html')

def about(request):
    return render(request, 'daystarApp/about.html')

def dolls(request):
    return render(request, 'daystarApp/dolls.html')


def baby(request):   
   
    getbabyform = AddBabyForm()
    BabeForm = AddBabyForm(request.POST)
    if request.method == 'POST':
        if AddBabyForm.is_valid():
            AddBabyForm.save()
            return HttpResponseRedirect(reverse('home'))
    return render(request, 'daystarApp/babe.html', {'getbabyform': getbabyform})
    


def payment(request):
    getpaymentform = AddPaymentForm()
    return render(request, 'daystarApp/payments.html', {'getpaymentform': getpaymentform})
        
def contact(request):
    return render(request, 'daystarApp/contact.html')

def sitters(request):
    return render(request, 'daystarApp/sitters.html')

def sitter_registration(request):
    return render(request, 'daystarApp/sitter_registration.html')

def baby_registration(request):
    return render(request, 'daystarApp/baby_registration.html')