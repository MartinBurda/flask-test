import flask
from flask import Blueprint, request, redirect, url_for, flash, render_template
from app import db
from app.db import db_execute
bp = Blueprint('login', __name__, url_prefix='/login')
@bp.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        command = "SELECT username FROM users WHERE username = ? AND password = ?"
        result = db_execute(command, (username,password))

        if result:
            flask.flash("Login successful")
        else:
            flask.flash("Login unsuccessful")
    return render_template("login.html")

@bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        command = "SELECT username FROM users WHERE username = ?"
        result = db_execute(command, (username,))
        if not result :
            command = "INSERT INTO users (username, password) VALUES (?, ?)"
            result = db_execute(command, (username,password))
            flask.flash("register successful")
        else:
            flask.flash("User already exists")
    return render_template("register.html")

@bp.route("/users")
def user_list():
    command = "SELECT * FROM users"
    result = db_execute(command)
    print(result)
    return render_template("user.html", result=result)