from flask import Blueprint, render_template, flash, redirect, request
from connection import db
from definitions.categorias import Categoria, CategoriaForm

categorias_routes = Blueprint('categorias', __name__)

@categorias_routes.route('/categorias', methods=['GET', 'POST'])
def categorias():
    form = CategoriaForm()
    if form.validate_on_submit():
        existing_categoria = Categoria.query.filter_by(name=form.name.data).first()
        if existing_categoria:
            flash('O nome da categoria já existe. Por favor, escolha outro.', 'danger')

        if existing_categoria is None:
            new_categoria = Categoria(name=form.name.data)
            db.session.add(new_categoria)
            db.session.commit()
            flash('Categoria criada com sucesso.', 'success')

    categorias_list = Categoria.query.all()
    return render_template('categorias.html', form=form, categorias=categorias_list)