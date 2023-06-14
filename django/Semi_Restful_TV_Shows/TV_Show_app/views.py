from django.shortcuts import render, redirect
from TV_Show_app.models import Show
from django.contrib import messages
# Create your views here.

def index(request):
    context = {
        'shows' : Show.objects.all()
    }
    return render(request, 'index.html', context)

def new_show(request):
    return render(request, 'new_show.html')

def create_new_show(request):
    # Validate Creating new Show
    errors = Show.objects.new_show_validate(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request,value)
        return redirect('/show/new')
    else:
        Show.objects.create(title =request.POST['title']
                            ,network = request.POST['network']
                            ,desc = request.POST['desc']
                            ,release_date = request.POST['release_date']
                            ) 
        id = Show.objects.last()
        return redirect('/show/' + str(id.id))

def show_details(request, id):
    context = {
        'show' : Show.objects.get(id = id)
    }
    return render(request, 'show_details.html', context)

def show_edit(request, id):
    show = Show.objects.get(id = id)
    date = str(show.release_date)
    #value="2013-01-08" This is the format we need to send to the input type date in html in order to be able to change its value
    context = {
        'show' : show,
        'date' : date,
    }
    return render (request, 'show_edit.html',context)

def show_update(request,id):
    # Validate Editing Show
    errors = Show.objects.new_show_validate(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request,value)
        return redirect('/show/'+ str(id) +'/edit')
    else:
        show_to_update = Show.objects.get(id = id)
        show_to_update.title = request.POST['title']
        show_to_update.network = request.POST['network']
        show_to_update.release_date = request.POST['release_date']
        show_to_update.desc = request.POST['desc']
        show_to_update.save()
        return redirect('/')

def show_delete(request,id):
    show_to_delete = Show.objects.get(id = id)
    show_to_delete.delete()
    return redirect('/')
