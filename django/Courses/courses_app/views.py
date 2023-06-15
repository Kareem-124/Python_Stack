from django.shortcuts import render, redirect
from courses_app.models import Courses,Comments
from django.contrib import messages
def index(request):
    context = {
        'courses' : Courses.objects.all()
    }
    return render(request, 'index.html', context)

def add_course(request):
    # Validate The Posted Data from the form
    error = Courses.objects.error_check(request.POST)
    # Check if there exists any error massage
    if len(error) > 0:
        for key, value in error.items():
            messages.error(request,value)
        return redirect('/')
    # Create the object if no errors exists
    else:
        new_course = Courses.objects.create(name = request.POST['name'], desc = request.POST['desc'])
        return redirect('/')

def comment_page(request,id):
    return redirect('/')

def delete_course(request,id):
    course_delete = Courses.objects.get(id=id)
    course_delete.delete()
    return redirect('/')



