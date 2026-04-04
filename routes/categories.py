from flask import Blueprint, render_template, flash, redirect, request
from connection import db
from definitions.categories import Category, CategoryForm

categories_routes = Blueprint('categories',__name__)

@categories_routes.route('/categories', methods=['GET', 'POST'])
def categorias():
    form = CategoryForm()

    if form.validate_on_submit():
        new_categoria = Category(
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

    categorias_list = Category.query.all()
    return render_template('categorias.html', form=form, categorias=categorias_list)