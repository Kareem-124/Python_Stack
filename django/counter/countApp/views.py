from django.shortcuts import render, redirect

global flag
flag = True

def index(request):
    global flag
    if flag:
        request.session['counter_index'] = 0
        request.session['user_counter'] = 0
        request.session['refresh_counter'] = 0
        request.session['placeholder_text'] = 'Enter the number of wanted visits'
        request.session['color'] = ''
        flag = False
    request.session['counter_index'] +=1
    request.session['refresh_counter'] +=1
    context = {
        'counter_index' : request.session['refresh_counter'] + request.session['user_counter'] ,
        'user_counter' : request.session['user_counter'],
        'refresh_counter' : request.session['refresh_counter'],
        'placeholder_text': request.session['placeholder_text'],
        'color': request.session['color'],
    }
    return render(request, 'index.html', context)
# Create your views here.

def process(request):
    if request.POST['form_type'] == 'increment':
        request.session['counter_index'] +=1
        request.session['user_counter'] +=2
        return redirect('/')
    
    if request.POST['user_counter'] =='':
        request.session['color'] = 'color'
        request.session['placeholder_text'] = 'Please Make sure you enter only numbers !!'
        request.session['counter_index'] -=1
        request.session['refresh_counter'] -=1
        return redirect('/')

    
    request.session['counter_index'] += int(request.POST['user_counter'])
    request.session['user_counter'] += int(request.POST['user_counter'])
    request.session['placeholder_text'] = 'Enter the number of wanted visits'
    request.session['color'] = ''
    return redirect('/')

def reset(request):
    global flag
    flag = True
    return redirect('/')