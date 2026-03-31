from flask import Blueprint, render_template,flash, redirect, request
from connection import db
from flask_login import login_user, logout_user,current_user
from definitions.user import User, RegisterForm, LoginForm
from connection import db

auth_routes =  Blueprint('auth', __name__)


@auth_routes.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect('/')

    form = RegisterForm()
    if request.method == "GET":
        form.name.data = request.args.get('name', '')
        form.email.data = request.args.get('email', '')
        form.password.data = request.args.get('password', '')
        form.telephone.data = request.args.get('telephone', '')
        form.address.data = request.args.get('address', '')

    if form.validate_on_submit():
        existing_user = User.query.filter_by(username=form.username.data).first()
        if existing_user:
            flash('O nome de usuário já existe. Por favor, escolha outro.', 'danger')
            return render_template('register.html', form=form)

        new_user = User(username=form.username.data)
        new_user.set_password(form.password.data)
        db.session.add(new_user)
        db.session.commit()
        flash('Cadastro realizado com sucesso. Faça login.', 'success')
        return redirect('/auth/login')

    return render_template('register.html', form=form)

@auth_routes.route('/login', methods=['GET', 'POST'])
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
            flash('Nome de usuário ou senha inválidos.', 'danger')

    return render_template('login.html', form=form)

@auth_routes.route('/logout')
def logout():
    logout_user()
    flash('Logout efetuado com sucesso.', 'success')
    return redirect('/auth/login')

