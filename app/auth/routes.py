from flask import render_template, flash, redirect
from flask_login import login_user, logout_user, current_user
from app.extensions import db
from .models import User
from .forms import LoginForm, RegisterForm
from . import auth_bp


@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect('/')

    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and user.check_password(form.password.data):
            login_user(user)
            flash('Login efetuado com sucesso.', 'success')
            return redirect('/')
        else:
            flash('Nome de usuario ou senha invalidos.', 'danger')

    return render_template('auth/login.html', form=form)


@auth_bp.route('/logout')
def logout():
    logout_user()
    flash('Logout efetuado com sucesso.', 'success')
    return redirect('/auth/login')


@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()

    if form.validate_on_submit():
        existing_user = User.query.filter_by(email=form.email.data).first()

        if existing_user:
            flash('O Email de usuario ja existe. Por favor, escolha outro.', 'danger')
            return render_template('auth/register.html', form=form)

        new_user = User(
            username=form.username.data,
            email=form.email.data,
            phone=form.telephone.data,
            address=form.address.data
        )
        new_user.set_password(form.password.data)

        db.session.add(new_user)
        db.session.commit()

        flash('Cadastro realizado com sucesso. Faca login.', 'success')
        return redirect('/auth/login')

    return render_template('auth/register.html', form=form)
