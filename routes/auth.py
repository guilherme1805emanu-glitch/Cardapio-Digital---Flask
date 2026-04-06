from flask import Blueprint, render_template,flash, redirect
from flask_login import login_user, logout_user,current_user
from definitions.user import User, LoginForm

auth_routes =  Blueprint('auth', __name__)

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

