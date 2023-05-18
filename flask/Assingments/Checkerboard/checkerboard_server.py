from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', row = 8, block = 8)

@app.route('/4')
def four():
    return render_template('index.html', row = 8, block = 4)

@app.route('/<row>/<block>')
def custom(row,block):
    return render_template('index.html', row = int(row), block = int(block))

if __name__ == "__main__":
    app.run(debug = True)



