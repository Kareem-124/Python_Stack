from flask import Flask, render_template, redirect, request, session
import random
from init import init

app = Flask(__name__)
app.secret_key = '1234'




@app.route('/')
def index():
    global init
    if init == True:
        
        session['game_running'] = False
        session['class'] = "bg-primary-subtle" 
        session['massage'] = "Start The Game"
        session['button_massage'] = "Start"
        session['box_massage'] = "Enter Your Number"
        session['disabled'] = ''
        init = False

    if session['game_running'] == False:
        session['class'] = "bg-primary-subtle" 
        session['massage'] = "Start The Game"
    
    return render_template('index.html'
                        ,bg_class = session['class']
                        ,massage = session['massage']
                        ,button_massage = session['button_massage']
                        ,box_massage = session['box_massage']
                        ,disable = session['disabled'] )

@app.route('/check', methods = ['POST'])
def check():
    if session['button_massage'] == "Restart":
        global init
        init = True
        return redirect('/')

    user_input = request.form['user_input']
    if user_input.isnumeric():
        session['box_massage'] = "Enter Your Number"
        if session['button_massage'] == "Start":                # Start the game flag and get a random number
            session['game_running'] = True
            session['random_num'] = random.randint(1 , 100)
            session['button_massage'] = "Check !"
        
        
        if int(user_input)  == session['random_num']:            # if the user answer is right
            session['class'] = "bg-success"
            session['massage'] = "Great ! You did it !!!"
            session['button_massage'] = "Restart"
            session['disabled'] = 'disabled'
            return redirect('/')
        else:                                               # if the user answer is wrong
            session['class'] = "bg-danger"
            if int(user_input) > session['random_num']:
                session['massage'] = "Too High !"
            else:
                session['massage'] = "Too Low !"
            return redirect('/')
    else:
        session['class'] = "bg-warning"
        session['box_massage'] = "!!!Please Only Enter Numbers!!!"
        session['massage'] = "We Only Take Numbers In This Game"
        return redirect('/')

if __name__ == "__main__":
    app.run(debug = True)