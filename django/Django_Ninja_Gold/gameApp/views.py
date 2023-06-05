from django.shortcuts import render, redirect
import random
import datetime


global init
init = True


def appended(arry,obj):
    arry.append(obj)
    print(f"arr value = {arry}")
    return arry

def index(request):
    global init
    if init:
        request.session['player_money'] = 0
        request.session['activity'] = []
        rev= []
        request.session['disabled'] = ' '
        request.session['moves'] = 15
        init = False
    if request.session['player_money'] >= 500:
        request.session['disabled'] = 'disabled'
        request.session['activity'].append(
f'<p class="bg-success done text-center win">  Well Done !! You won the round !</p>')
        request.session.modified = True
    if request.session['moves'] <= 0:
        request.session['disabled'] = 'disabled'
        request.session['activity'].append(f'<p class="bg-warning done text-center">  Game Over</p>')
        request.session.modified = True
        
        
    rev = request.session['activity']
    rev.reverse()
    print(f"Aactivity list = {(request.session['activity'])}")
    context = {
        'player_money':request.session['player_money'],
        'activity':rev,
        'activity_length':len(request.session['activity'])-1,
        'disabled':request.session['disabled'],
        'moves':request.session['moves'],
    }
    return render(request,'index.html',context)



def process_money(request):
    global init
    request.session['moves'] -= 1
    if request.POST['property'] == "farm":
        generate_money = random.randint(10, 20)
        request.session['player_money'] += generate_money
        date = datetime.datetime.now()
        request.session['activity'].append(f'<p class="green">  Made : ({generate_money} $)  from the Farms .... {date.strftime("%c")}</p>')
        request.session.modified = True
        
        return redirect('/')
    
    elif request.POST['property'] == "cave":
        generate_money = random.randint(5, 10)
        request.session['player_money'] += generate_money
        date = datetime.datetime.now()
        request.session['activity'].append(
            f'<p class="green">  Made : ({generate_money} $)  from the Cave .... {date.strftime("%c")}</p>')
        request.session.modified = True
        
        return redirect('/')
    
    elif request.POST['property'] == "house":
        generate_money = random.randint(2, 5)
        request.session['player_money'] += generate_money
        date = datetime.datetime.now()
        request.session['activity'].append(
            f'<p class="green">  Made : ({generate_money} $)  from the House .... {date.strftime("%c")}</p>')
        request.session.modified = True
        
        return redirect('/')
    
    elif request.POST['property'] == "market":
        generate_money = random.randint(-50, 50)
        request.session['player_money'] += generate_money
        if generate_money >= 0:
            date = datetime.datetime.now()
            request.session['activity'].append(
                f'<p class="green">  Made : ({generate_money} $)  from the Market .... {date.strftime("%c")}</p>')
            request.session.modified = True
            
        else:
            date = datetime.datetime.now()
            request.session['activity'].append(
                f'<p class="red">  Lost : ({generate_money} $)  from the Market .... Opps !  {date.strftime("%c")}</p>')
            request.session.modified = True
            
        return redirect('/')
    elif request.POST['property'] == "reset":
        init = True
        return redirect('/')

