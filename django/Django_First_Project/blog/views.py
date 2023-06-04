from django.shortcuts import render , HttpResponse , redirect
from django.http import JsonResponse
def root(request):
    return redirect("/blog")

def index(request):
    return HttpResponse ("Placeholder to latter display all the blog lists ")

def new(request):
    return HttpResponse ("placeholder to display a new form to create a new blog")

def create(request):
    return redirect("/")

def show(request,number):
    return HttpResponse(f"placeholder to display blog number: {number}")

def edit(request,number):
    return HttpResponse(f"placeholder to edit blog {number}")

def destroy(request,number):
    return redirect("/blog")

def json(request):
    context = {
        'title' : 'My first Blog',
        'content' : 'Lorem, ipsum dolor sit amet consectetur adispling elit.'
    }
    return JsonResponse(context)