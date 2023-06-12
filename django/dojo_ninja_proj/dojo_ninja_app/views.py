from django.shortcuts import render, redirect
from .models import ninja, dojo


def index(request):

    context = {
        'dojos': dojo.objects.all()
    }
    return render(request, 'index.html', context)


def process(request):
    # ADD a New Dojo process
    if request.POST['process'] == "add_dojo":
        dojo.objects.create(
            name=request.POST['dojo_name'], city=request.POST['city'], state=request.POST['state'])

    # Add A new Ninja
    elif request.POST['process'] == "add_ninja":
        dojo_id = dojo.objects.get(id=int(request.POST['choose_dojo']))
        ninja.objects.create(
            first_name=request.POST['first_name'], last_name=request.POST['last_name'], dojo_id=dojo_id)

    # Delete Dojo and there associated ninjas
    elif request.POST['process'] == "delete_dojo":
        # Get the id for the dojo to be deleted
        dojo_id = int(request.POST['dojo_name_to_delete'])
        delete_dojo = dojo.objects.get(id=dojo_id)  # Get the Dojo object
        # iterate through the ninjas in the selected dojo and delete them one by one from the Data Base
        for ninjas in delete_dojo.ninjas.all():
            ninjas.delete()
        delete_dojo.delete()  # delete the selected dojo object from Data Base

    return redirect('/')
