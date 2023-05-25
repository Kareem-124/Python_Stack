from flask import Flask, render_template, redirect, request, session
import random
import datetime
from init import init
app = Flask(__name__)
app.secret_key = '1234'


@app.route('/')
def index():
    global init
    if init == True:
        session['money'] = 0
        session['activity_list'] = []
        session['disabled'] = ' '
        session['num_move'] = 15
        init = False
    if session['money'] >= 500:
        session['disabled'] = 'disabled'
        session['activity_list'].append(
            f'<p class="bg-success done text-center win">  Well Done !! You won the round !</p>')
    if session['num_move'] <= 0:
        session['disabled'] = 'disabled'
        session['activity_list'].append(
            f'<p class="bg-warning done text-center">  Game Over</p>')

    return render_template('index.html'
                            , player_money=session['money']
                            , activity=session['activity_list']
                            , activity_length=len(session['activity_list'])-1
                            , disabled=session['disabled']
                            , moves=session['num_move']
                            )


@app.route('/process_money', methods=['POST'])
def process_money():
    global init
    session['num_move'] -= 1
    if request.form['property'] == "farm":
        generate_money = random.randint(10, 20)
        session['money'] += generate_money
        date = datetime.datetime.now()
        session['activity_list'].append(
            f'<p class="green">  Made : ({generate_money} $)  from the Farms .... {date.strftime("%c")}</p>')
        return redirect('/')
    
    elif request.form['property'] == "cave":
        generate_money = random.randint(5, 10)
        session['money'] += generate_money
        date = datetime.datetime.now()
        session['activity_list'].append(
            f'<p class="green">  Made : ({generate_money} $)  from the Cave .... {date.strftime("%c")}</p>')
        return redirect('/')
    
    elif request.form['property'] == "house":
        generate_money = random.randint(2, 5)
        session['money'] += generate_money
        date = datetime.datetime.now()
        session['activity_list'].append(
            f'<p class="green">  Made : ({generate_money} $)  from the House .... {date.strftime("%c")}</p>')
        return redirect('/')
    
    elif request.form['property'] == "market":
        generate_money = random.randint(-50, 50)
        session['money'] += generate_money
        if generate_money >= 0:
            date = datetime.datetime.now()
            session['activity_list'].append(
                f'<p class="green">  Made : ({generate_money} $)  from the Market .... {date.strftime("%c")}</p>')
        else:
            date = datetime.datetime.now()
            session['activity_list'].append(
                f'<p class="red">  Lost : ({generate_money} $)  from the Market .... Opps !  {date.strftime("%c")}</p>')
        return redirect('/')
    elif request.form['property'] == "reset":
        init = True
        return redirect('/')



if __name__ == "__main__":
    app.run(debug=True)
