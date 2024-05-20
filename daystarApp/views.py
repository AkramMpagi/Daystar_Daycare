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
from django.shortcuts import render, get_object_or_404


# Create your views here.


def result_detail(request, result_id):
    result = get_object_or_404(Sitter, pk=result_id)  # Replace YourModel with your actual model
    return render(request, 'daystarApp/result_detail.html', {'result': result})

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
    query = request.GET.get('query')
    results = []
    if query:
        results = Sitter.objects.filter(name__icontains=query)  
    return render(request, 'daystarApp/sitters.html', {'sitters': sitters, 'results': results, 'query': query})





def sitter_registration(request):
    # getsitterregistrationform = AddSitterRegistrationForm()
    if request.method == 'POST':
        name = request.POST['name']
        contact = request.POST['contact']
        # category = request.POST['category']
        # timeIn = request.POST['timeIn']
        # timeOut = request.POST['timeOut']
        date_of_birth = request.POST['date_of_birth']
        recommender_name = request.POST['recommender_name']
        level_of_education = request.POST['level_of_education']
        nin = request.POST['nin']
        sitter_number = request.POST['sitter_number']
        location = request.POST['location']
        next_of_kin = request.POST['next_of_kin']

        new_sitter = Sitter(name=name, contact=contact, date_of_birth=date_of_birth, recommender_name=recommender_name, level_of_education=level_of_education, nin=nin, sitter_number=sitter_number, location=location, next_of_kin=next_of_kin)








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
        brought_by = request.POST.get('brought_by')
        time_of_arrival = request.POST.get('time_of_arrival')
        period_of_stay = request.POST.get('period_of_stay')
        fees = request.POST.get('fees')
        baby_number = request.POST.get('baby_number')

        new_baby = Baby(name=name, gender=gender, age=age, location=location, father_name=father_name, mother_name=mother_name, brought_by=brought_by, time_of_arrival=time_of_arrival, period_of_stay=period_of_stay, fees=fees, baby_number=baby_number)
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






