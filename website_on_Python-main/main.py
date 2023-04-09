from flask import Flask, render_template, redirect, request
from data import db_session
from data.users import User
from data.jobs import Jobs
import requests
from data.forms import RegisterForm, LoginForm
from flask_login import LoginManager, login_user, logout_user, login_required
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret_key'
login_manager = LoginManager()
login_manager.init_app(app)


@login_manager.user_loader
def load_user(id):
    db_sess = db_session.create_session()
    return db_sess.query(User).get(id)


@app.route('/')
def index():
    session = db_session.create_session()
    jobs = session.query(Jobs).all()
    return render_template("index.html", jobs=jobs)


@app.route('/maths')
def maths():
    with open('templates/maths.html', 'r', encoding='utf-8') as file:
        return file.read()


@app.route('/algebra')
def algebra():
    with open('templates/algebra.html', 'r', encoding='utf-8') as file:
        return file.read()


@app.route('/algebra/log')
def log():
    with open('templates/log.html', 'r', encoding='utf-8') as file:
        return file.read()


@app.route('/algebra/nerav')
def nerav():
    with open('templates/nerav.html', 'r', encoding='utf-8') as file:
        return file.read()


@app.route('/algebra/trigo')
def trigo():
    with open('templates/trigo.html', 'r', encoding='utf-8') as file:
        return file.read()


@app.route('/algebra/urav')
def urav():
    with open('templates/urav.html', 'r', encoding='utf-8') as file:
        return file.read()


@app.route('/algebra/funct')
def funct():
    with open('templates/funct.html', 'r', encoding='utf-8') as file:
        return file.read()


@app.route('/physics')
def physics():
    with open('templates/physics.html', 'r', encoding='utf-8') as file:
        return file.read()


@app.route('/physics/kinematika')
def kinematika():
    with open('templates/kinematika.html', 'r', encoding='utf-8') as file:
        return file.read()


@app.route('/physics/dinamika')
def dinamika():
    with open('templates/dinamika.html', 'r', encoding='utf-8') as file:
        return file.read()


@app.route('/physics/kolebania')
def kolebania():
    with open('templates/kolebania.html', 'r', encoding='utf-8') as file:
        return file.read()


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect("/")


def main():
    name_db = 'mars_explorer.db'
    db_session.global_init(f"db/{name_db}")
    app.run(port=5000, host='127.0.0.1')


if __name__ == '__main__':
    main()
