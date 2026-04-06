from flask import Blueprint, flash, redirect, render_template, request
from definitions.user import User, RegisterForm
from connection import db


app_welcome = Blueprint('welcome', __name__)

@app_welcome.route('/welcome', methods=['GET', 'POST'])
def route_welcome():
    form = RegisterForm()

    if form.validate_on_submit():
        existing_user = User.query.filter_by(email=form.email.data).first()

        if existing_user:
            flash('O Email de usuário já existe. Por favor, escolha outro.', 'danger')
            return render_template('welcome.html', form=form)
        
        new_user = User(
            username=form.username.data,
            email=form.email.data,
            phone=form.telephone.data,
            address=form.address.data
        )

        new_user.set_password(form.password.data)

        db.session.add(new_user)
        db.session.commit()

        flash('Cadastro realizado com sucesso. Faça login.', 'success')
        return redirect('/auth/login')

    return render_template("welcome.html", form=form)