from .forms import RegisterForm, LoginForm
from flask import render_template, redirect, url_for, flash
from . import auth

@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash("Successfully logged in", 'success')
        return redirect(url_for('main.profile'))
    return render_template('auth/login.html', form=form)

@auth.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        return redirect(url_for('auth.login'))
    return render_template('auth/register.html', form=form)