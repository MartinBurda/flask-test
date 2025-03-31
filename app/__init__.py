from flask import Flask, render_template

"""
Tajný klíč, spojení s databází
"""
app = Flask(__name__, template_folder='../templates', static_folder='../static')
app.config['SECRET_KEY'] = 'rtzuioijhgfdsxcvbnjhgfdcvbhztrfdc'
app.config['DATABASE'] = "database.sqlite"

"""
index
"""
@app.route('/')
def index():
    return render_template('index.html')


