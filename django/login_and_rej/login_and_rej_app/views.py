from django.shortcuts import render, redirect
from login_and_rej_app.models import *
from django.contrib import messages
import bcrypt

# Create your views here.

def index(request):

    return render(request, 'index.html')

def login(request):
    # see if the username provided exists in the database
    user = Users.objects.filter(email=request.POST['email']) 
    if user: 
        logged_user = user[0] 
        if bcrypt.checkpw(request.POST['password'].encode(), logged_user.password.encode()):
            # if we get True after checking the password, we may put the user id in session
            request.session['user_id'] = logged_user.id
            messages.success(request,"You have Successfully logged in")
            return redirect('/success')
        else:
            # if we didn't find anything in the database by searching by username or if the passwords don't match, 
            messages.error(request,"Email or Password incorrect")
            return redirect('/')
    else:
        # if we didn't find anything in the database by searching by username or if the passwords don't match, 
        messages.error(request,"Email or Password incorrect")
        return redirect('/')

def success(request):
    user = Users.objects.get(id = request.session['user_id'])
    context ={
        'first_name' : user.first_name,
        'last_name' : user.last_name,

    }
    return render(request, 'success.html', context)

def reg_process(request):
    # Validation Part Is here
    error = Users.objects.validate(request.POST)
    if len(error) > 0:
        for key, value in error.items():
            messages.error(request,value)
        return redirect('/')
    else:
        password = request.POST['password']
        ps_hash = bcrypt.hashpw(password.encode(),bcrypt.gensalt()).decode()
        Users.objects.create(
            first_name = request.POST['first_name']
            ,last_name = request.POST['last_name']
            ,email = request.POST['email']
            ,password = ps_hash
        )
        messages.success(request,"User has been created Successfully!")
        return redirect ('/')

def logout(request):
    list(messages.get_messages(request))
    request.session.flush()
    return redirect('/')