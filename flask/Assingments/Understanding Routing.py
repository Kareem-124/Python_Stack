from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Hello World"

@app.route("/dojo")
def hello_dojo():
    return "Dojo"


@app.route("/say/<name>")
def say(name):
    return "Hi " + name +"!"

@app.route("/repeat/<int:number>/<text>")
def repeat(number,text):
    return (text + " ") * number

@app.errorhandler(404)
def page_not_found(e):
    # return a custom error message for 404 errors
    return "Sorry! No response. Try again.", 404

if __name__ == "__main__":
    app.run(debug = True)

