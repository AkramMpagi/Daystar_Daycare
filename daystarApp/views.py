from django.shortcuts import render, redirect
from daystarApp import views
from django.http import HttpResponse, HttpResponseRedirect
from . import urls
from .models import *
from .forms import *
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


# Create your views here.


def index(request):

    count_babies = Baby.objects.count()
    return render(request, 'daystarApp/index.html', {'count_babies': count_babies})



def about(request):
    return render(request, 'daystarApp/about.html')

def dolls(request):
    getdollform = AddDollForm()
    return render(request, 'daystarApp/dolls.html', {'getdollform': getdollform})


def baby(request):
    babies = Baby.objects.all()
    return render(request, 'daystarApp/babies.html', {'babies': babies})
    


def payment(request):
    if request.method == 'POST':
        getpaymentform = AddPaymentForm(request.POST)
        if getpaymentform.is_valid():
            getpaymentform.save()
            return redirect('home')
    else:
        getpaymentform = AddPaymentForm()
    return render(request, 'daystarApp/payments.html', {'getpaymentform': getpaymentform})
       
def contact(request):
    return render(request, 'daystarApp/contact.html')



def sitters(request):
    sitters = Sitter.objects.all()
    return render(request, 'daystarApp/sitters.html', {'sitters': sitters})





def sitter_registration(request):
    # getsitterregistrationform = AddSitterRegistrationForm()
    if request.method == 'POST':
        name = request.POST['name']
        contact = request.POST['contact']
        # category = request.POST['category']
        timeIn = request.POST['timeIn']
        timeOut = request.POST['timeOut']
        new_sitter = Sitter(name=name, contact=contact, timeIn=timeIn, timeOut=timeOut)
        new_sitter.save()
        messages.success(request, 'You have successfully created a new sitter')
        return redirect('sitters')
    return render(request, 'daystarApp/sitter_registration.html')







def baby_registration(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        gender = request.POST.get('gender')
        age = request.POST.get('age')
        location = request.POST.get('location')
        father_name = request.POST.get('father_name')
        mother_name = request.POST.get('mother_name')
        new_baby = Baby(name=name, gender=gender, age=age, location=location, father_name=father_name, mother_name=mother_name)
        new_baby.save()
        messages.success(request, 'You have successfully created a new baby')
        return redirect('baby')
 
    return render(request, 'daystarApp/baby_registration.html')






def doll(request):
    getdollform = AddDollForm()
    return render(request, 'daystarApp/doll.html', {'getdollform': getdollform})


def doll_store(request):
    return render(request, 'daystarApp/doll_store.html')



def doll_sales(request):
    return render(request, 'daystarApp/doll_sales.html')




def otherplay_tools(request):
    return render(request, 'daystarApp/otherplay_tools.html')




def invoices(request):
    return render(request, 'daystarApp/invoices.html')




def all_transactions(request):
    return render(request, 'daystarApp/all_transactions.html')




def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, f'Welcome back {username}!')
            return redirect('home')
        else:
            messages.error(request, 'Invalid username or password')
            
    return render(request, 'daystarApp/login.html')






def logout_user(request):
    logout(request)
    messages.success(request, 'You have successfully logged out')
    return redirect('login')






