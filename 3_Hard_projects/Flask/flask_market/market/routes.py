from market import app
from flask import render_template, redirect, url_for, flash
from market.models import Item, User
from market.forms import RegisterForm, LoginForm
from market import db
from flask_login import login_user, logout_user, login_required

@app.route('/')
@app.route('/home')
def homePage():
    return render_template('home.html')

@app.route('/market')
@login_required
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
        login_user(userToCreate)
        flash(f'Account created successfully! You are now logged in as {userToCreate.username}', category='success')
        return redirect(url_for('marketPage'))
    if form.errors != {}: # if there are not errors from validation
        for err_msg in form.errors.values():
            flash(f'There was an error with creating a user: {err_msg}', category='danger')
    return render_template('register.html',form=form)

@app.route('/login', methods=['GET','POST'])
def loginPage():
    form = LoginForm()
    if form.validate_on_submit():
        attemptedUser = User.query.filter_by(username=form.username.data).first()
        if attemptedUser and attemptedUser.check_password_correction(attempted_password=form.password.data):
            login_user(attemptedUser)
            flash(f'Success! You are logged in as: {attemptedUser.username}', category='success')
            return redirect(url_for('marketPage'))
        else:
            flash('Username and password are not match! Please try again', category='danger')
            
    return render_template('login.html', form=form)

@app.route('/logout')
def logoutPage():
    logout_user()
    flash('You have been logged out!', category='info')
    return redirect(url_for('homePage'))