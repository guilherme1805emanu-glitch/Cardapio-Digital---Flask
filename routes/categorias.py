from flask import Blueprint, render_template, flash, redirect, request
from connection import db
from definitions.categorias import Categoria, CategoryForm, CategoryType

categories_routes = Blueprint('categorias',__name__)

@categories_routes.route('/categorias', methods=['GET', 'POST'])
def categorias():
    form = CategoryForm()

    if form.validate_on_submit():
        new_categoria = Categoria(
            name=form.name.data,
            category_type=form.category_type.data
        )

        try:
            db.session.add(new_categoria)
            db.session.commit()
            flash('Categoria criada com sucesso.', 'success')
        except Exception:
            db.session.rollback()
            flash('Erro ao salvar categoria.', 'danger')

        return redirect(request.url)

    categorias_list = Categoria.query.all()
    return render_template('categorias.html', form=form, categorias=categorias_list)