from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/abc')
def abc():
    return render_template('abc.html')

@app.route('/alfa')
def alfa():
    return render_template('alfa.html')

@app.route('/azb')
def azb():
    return render_template('azb.html')

@app.route('/heb')
def heb():
    return render_template('heb.html')

@app.route('/odkaz', methods=['GET', 'POST'])
def link():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        radio = request.form['radio']
        return render_template("zkouska.html", username=username, password=password, radio=radio)
    return render_template('link.html')

@app.route('/nasobek/<n1>/<n2>')
def hello(n1, n2):
    try:
        n1 = int(n1)
        n2 = int(n2)
    except ValueError:
        return '<h1>špatná čísla</h1>'

    n3 = n1 * n2
    return f'<h1>Násobek je: {n3}</h1>'


if __name__ == '__main__':
    app.run()
