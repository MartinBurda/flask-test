from functools import wraps

import flask
from flask import Blueprint, request, redirect, url_for, flash, render_template, session
from app import db
from app.db import db_execute
bp = Blueprint('login', __name__, url_prefix='/login')

"""
Funkce pro odhlášení
"""
@bp.route("/logout")
def logout():
    session.pop("username", None)
    flash("You have been logged out")
    return redirect(url_for("index"))
@bp.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        command = "SELECT username FROM users WHERE username = ? AND password = ?"
        result = db_execute(command, (username,password))

        if result:
            session["username"] = username
            flask.flash("Login successful")
        else:
            flask.flash("Login unsuccessful")
    return render_template("login.html")

"""
Funkce pro registraci
"""
@bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        password1 = request.form['password1']
        email = request.form['email']

        command = "SELECT username FROM users WHERE username = ?"
        result = db_execute(command, (username,))
        if not result :
            if password == password1:
                command = "INSERT INTO users (username, password,email) VALUES (?, ?, ?)"
                result = db_execute(command, (username,password,email))
                flask.flash("register successful")
            else:
                flask.flash("passwords doesn't match")
        else:
            flask.flash("User already exists")
    return render_template("register.html")

"""
session - zamezení přístupu k určitým stránkám...
"""
def login_required(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if "username" not in session:
            flask.flash("You need to login first")
            return redirect(url_for("login.login"))
        return func(*args, **kwargs)
    return wrapper