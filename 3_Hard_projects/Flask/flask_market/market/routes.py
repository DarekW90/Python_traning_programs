from market import app
from flask import render_template
from market.models import Item
from market.forms import RegisterForm

@app.route('/')
@app.route('/home')
def homePage():
    return render_template('home.html')

@app.route('/market')
def marketPage():
    items = Item.query.all()
    return render_template('market.html',items=items)

@app.route('/register')
def registerPage():
    form = RegisterForm()
    return render_template('register.html',form=form)