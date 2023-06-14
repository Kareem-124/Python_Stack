from django.shortcuts import render, redirect
from .models import users

def index(request):
    context = {
        'users_data' : users.objects.all()
    }
    return render(request, "index.html", context)

def add_user(request):
    first_name_form = request.POST['first_name']
    last_name_form = request.POST['last_name']
    email_address_form = request.POST['email_address']
    age_form = request.POST['age']

    users.objects.create(first_name= first_name_form, last_name = last_name_form, email_address = email_address_form, age = age_form)
    
    return redirect('add_user')
