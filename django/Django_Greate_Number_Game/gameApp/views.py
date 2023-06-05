from django.shortcuts import render, redirect
import random
global init
init = True

def index(request):
    global init
    if init == True:
        
        request.session['game_running'] = False
        request.session['class'] = "bg-primary-subtle" 
        request.session['massage'] = "Start The Game"
        request.session['button_massage'] = "Start"
        request.session['box_massage'] = "Enter Your Number"
        request.session['disabled'] = ''
        init = False

    if request.session['game_running'] == False:
        request.session['class'] = "bg-primary-subtle" 
        request.session['massage'] = "Start The Game"
    
    context = {
        'bg_class' : request.session['class'], 
        'massage' : request.session['massage'], 
        'button_massage' : request.session['button_massage'], 
        'box_massage' : request.session['box_massage'], 
        'disable' : request.session['disabled'], 
    }
    return render(request,'index.html',context)


def check(request):
    if request.session['button_massage'] == "Restart":
        global init
        init = True
        return redirect('/')

    user_input = request.POST['user_input']
    if user_input.isnumeric():
        request.session['box_massage'] = "Enter Your Number"
        if request.session['button_massage'] == "Start":                # Start the game flag and get a random number
            request.session['game_running'] = True
            request.session['random_num'] = random.randint(1 , 100)
            request.session['button_massage'] = "Check !"
        
        
        if int(user_input)  == request.session['random_num']:            # if the user answer is right
            request.session['class'] = "bg-success"
            request.session['massage'] = "Great ! You did it !!!"
            request.session['button_massage'] = "Restart"
            request.session['disabled'] = 'disabled'
            return redirect('/')
        else:                                               # if the user answer is wrong
            request.session['class'] = "bg-danger"
            if int(user_input) > request.session['random_num']:
                request.session['massage'] = "Too High !"
            else:
                request.session['massage'] = "Too Low !"
            return redirect('/')
    else:
        request.session['class'] = "bg-warning"
        request.session['box_massage'] = "!!!Please Only Enter Numbers!!!"
        request.session['massage'] = "We Only Take Numbers In This Game"
        return redirect('/')
