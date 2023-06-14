from django.shortcuts import render, redirect
from TV_Show_app.models import Show
# Create your views here.

def index(request):
    context = {
        'shows' : Show.objects.all()
    }
    return render(request, 'index.html', context)

def new_show(request):
    return render(request, 'new_show.html')

def create_new_show(request):
    #Validation Section will be here
    Show.objects.create(title =request.POST['new_title']
                        ,network = request.POST['new_network']
                        ,desc = request.POST['new_desc']
                        ,release_date = request.POST['new_release_date']
                        ) 
    return redirect('/')

def show_details(request, id):
    context = {
        'show' : Show.objects.get(id = id)
    }
    return render(request, 'show_details.html', context)

def show_edit(request, id):
    context = {
        'show' : Show.objects.get(id = id)
    }
    return render (request, 'show_edit.html',context)

def show_update(request,id):
    show_to_update = Show.objects.get(id = id)
    show_to_update.title = request.POST['edit_title']
    show_to_update.network = request.POST['edit_network']
    show_to_update.release_date = request.POST['edit_release_date']
    show_to_update.desc = request.POST['edit_desc']
    show_to_update.save()
    return redirect('/')

def show_delete(request,id):
    show_to_delete = Show.objects.get(id = id)
    show_to_delete.delete()
    return redirect('/')
