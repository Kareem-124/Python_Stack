from flask import Flask, render_template, redirect, request
app=Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process_form():
    print("I entered the process form function!!! ")
    print(request.form)

if __name__ == "__main__":
    app.run(debug =True)