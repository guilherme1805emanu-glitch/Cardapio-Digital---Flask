from flask import render_template, flash, redirect, request
from app.extensions import db
from .models import Category
from .forms import CategoryForm
from . import categories_bp


@categories_bp.route('/', methods=['GET', 'POST'])
def index():
    form = CategoryForm()

    if form.validate_on_submit():
        new_category = Category(
            name=form.name.data,
            category_type=form.category_type.data
        )

        try:
            db.session.add(new_category)
            db.session.commit()
            flash('Categoria criada com sucesso.', 'success')
        except Exception:
            db.session.rollback()
            flash('Erro ao salvar categoria.', 'danger')

        return redirect(request.url)

    categories_list = Category.query.all()
    return render_template('categories/categories.html', form=form, categorias=categories_list)
