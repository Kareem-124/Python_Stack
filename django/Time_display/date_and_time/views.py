from django.shortcuts import render, redirect
from datetime import datetime

def index(request):
    return render(request, "index.html")
# Create your views here.

def time_display(request):
    now = datetime.now()
    date = now.strftime("%B %d, %Y")
    time= now.strftime("%H:%M %p")
    context = {
        'date': date,
        'time': time
    }
    return render(request,'index.html', context )
