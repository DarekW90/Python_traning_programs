from market import app
from flask import render_template, redirect, url_for, flash
from market.models import Item, User
from market.forms import RegisterForm
from market import db

@app.route('/')
@app.route('/home')
def homePage():
    return render_template('home.html')

@app.route('/market')
def marketPage():
    items = Item.query.all()
    return render_template('market.html',items=items)

@app.route('/register', methods=['GET','POST'])
def registerPage():
    form = RegisterForm()
    if form.validate_on_submit():
        userToCreate = User(username=form.username.data,
                            emailAddress = form.emailAddress.data,
                            password=form.password1.data)
        db.session.add(userToCreate)
        db.session.commit()
        return redirect(url_for('marketPage'))
    if form.errors != {}: # if there are not errors from validation
        for err_msg in form.errors.values():
            flash(f'There was an error with creating a user: {err_msg}', category='danger')
    return render_template('register.html',form=form)