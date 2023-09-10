from market import app
from flask import render_template, redirect, url_for, flash, request
from market.models import Item, User
from market.forms import RegisterForm, LoginForm, PurchaseItemForm, SellItemForm
from market import db
from flask_login import login_user, logout_user, login_required, current_user

@app.route('/')
@app.route('/home')
def homePage():
    return render_template('home.html')

@app.route('/market', methods=['GET','POST'])
@login_required
def marketPage():
    purchase_form = PurchaseItemForm()
    selling_form = SellItemForm()
    if purchase_form.validate_on_submit():
        if request.method == 'POST':
            # Purchase Item Logic
            purchased_item = request.form.get('purchased_item')
            p_item_object = Item.query.filter_by(name=purchased_item).first()
            if p_item_object:
                if current_user.can_purchase(p_item_object):
                    p_item_object.buy(current_user)
                    flash(f'Congratulations! You purchased {p_item_object.name} for {p_item_object.price}$', category='success')
                else:
                    flash(f'Unfortunetly, you dont have enough money to purchase {p_item_object.name}', category='danger')
            
            # Sell Item Logic
            sold_item=request.form.get('sold_item')
            s_item_object = Item.query.filter_by(name=sold_item).first()
            if s_item_object:
                if current_user.can_sell(s_item_object):
                    s_item_object.sell(current_user)
                    flash(f'Congratulations! You sold {s_item_object.name} back to market!', category='success')
                else:
                    flash(f'Something went wrong with seling {s_item_object.name}', category='danger')
            
            return redirect(url_for('marketPage'))
                
    if request.method == "GET":
        items = Item.query.filter_by(owner = None)
        owned_items = Item.query.filter_by(owner=current_user.id)
    return render_template('market.html',items=items, purchase_form=purchase_form, owned_items=owned_items, selling_form = selling_form)

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