from flask import Blueprint, flash, redirect, render_template, request
from flask_login import current_user
from definitions.user import User, RegisterForm
from connection import db


app_inicio = Blueprint('inicio', __name__)

@app_inicio.route('/' , methods=['GET', 'POST'])
def route1():
    form = RegisterForm(request.form)

    if form.validate_on_submit():
        existing_user = User.query.filter_by(email=form.name.data).first()

        if existing_user:
            flash('O nome de usuário já existe. Por favor, escolha outro.', 'danger')
            return render_template('incio.html', form=form)
        
        existing_email = User.query.filter_by(email=form.email.data).first()

        if existing_email:
            flash('Este email já está cadastrado.', 'danger')
            return render_template("inicio.html", form=form)

        new_user = User(
            name=form.name.data,
            email=form.email.data,
            phone=form.telephone.data,
            address=form.address.data
        )

        new_user.set_password(form.password.data)

        db.session.add(new_user)
        db.session.commit()

        flash('Cadastro realizado com sucesso. Faça login.', 'success')
        return redirect('/auth/login')
        
    return render_template("inicio.html", form=form)
