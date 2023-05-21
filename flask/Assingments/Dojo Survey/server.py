from flask import Flask, render_template, redirect, request
app=Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process_form():
    if request.form['form_name'] == "":
        return "Please Enter Your name ! "
    else:
        return render_template('show.html'
                                ,show_name=request.form['form_name']
                                ,show_location=request.form['form_dojo_location']
                                ,show_fav_language = request.form['form_fav_language']
                                ,show_comment=request.form['form_comment'])

if __name__ == "__main__":
    app.run(debug =True)