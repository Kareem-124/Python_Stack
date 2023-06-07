from django.shortcuts import render, HttpResponse, redirect

def index(request):
    return HttpResponse("placeholder to later display a list of all blogs")

def new(request):
    return HttpResponse("placeholder to display a new form to create a new blog")

def create(request):
    return redirect('/blogs')

def show(request, id):
    context = {
        'number' : f'<h1> placeholder to display blog number: {id} </h1>'
    }
    return render(request, "index.html" , context)

def edit_num(request, id):
    context = {
            'number' : f'<h1> placeholder to edit blog: {id} </h1>'
        }
    return render(request , "index.html", context)
    

def destroy(request, id):
    return redirect('/blogs')
