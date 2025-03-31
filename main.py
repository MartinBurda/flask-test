from flask import render_template, request, flash, redirect, url_for
from app import app, login, db, library
from app.db import create_db
from os import path

app.register_blueprint(login.bp)
app.register_blueprint(library.bp)

"""
hlavní funkce
"""
if __name__ == '__main__':
    if not path.exists(app.config["DATABASE"]):
        create_db()
    print("inicializace databaze")
    app.run(debug=True)
