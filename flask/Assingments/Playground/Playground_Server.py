from flask import Flask, render_template

app = Flask(__name__)


@app.route('/play')
def index():
    return render_template('index.html', number=3, color="blue")


@app.route('/play/<number>')
def number(number):
    return render_template('index.html', number=int(number), color="blue")


@app.route('/play/<num>/<color>')
def color(num, color):
    return render_template('index.html', number=int(num), color=color)


if __name__ == "__main__":
    app.run(debug=True)
