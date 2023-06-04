from django.shortcuts import render, redirect

def index(request):
    return render(request, 'index.html')

def process(request):
    data_from_form = request.POST
    print(f"name: {data_from_form.get('form_name')}")
    context = {
        'show_name': data_from_form.get('form_name'),
        'show_location': data_from_form.get('form_dojo_location'),
        'show_fav_language': data_from_form.get('form_fav_language'),
        'show_comment': data_from_form.get('form_comment'),
    }
    return render(request, 'show.html', context)