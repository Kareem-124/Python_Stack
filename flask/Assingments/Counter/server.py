from flask import Flask, render_template, redirect, request, session
app = Flask(__name__)
app.secret_key = '1234'


@app.route('/')
def index():
    try:
        if session['increment'] >= 0:
            session['increment'] = session['increment'] + 1
        else:
            session['increment'] = 0
        return render_template('index.html', counter_index = session['increment'], user_counter =session['user_increment'])
    except:
        session['increment'] = 0
        session['user_increment'] = 0
        return render_template('new_session.html')


@app.route('/process',  methods=['POST'])
def process():
    if request.form['form_type'] == "user_increment":                   # The user entered a number to increment
        if  (request.form['user_counter']).isnumeric() == False:        # if the user didn't send numerical value 
            session['increment']-=1
            return redirect('/')
        session['increment'] += int(request.form['user_counter']) -1
        session['user_increment'] += int(request.form['user_counter'])
        return redirect('/')
    else:                                                               # the "increment by 2" button was pressed
        session['increment'] = session['increment'] + 1
        session['user_increment']+=2
        return redirect('/')

@app.route('/reset', methods = ['POST'])
def reset():
    reset_value = request.form['reset']
    print(f"The value of reset_value = {reset_value}")
    session['increment'] = 0
    session['user_increment'] = 0
    return redirect('/')

@app.route('/destroy_session')
def clear_session():
    session.clear()
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)
