from flask import render_template
from . import pizzas_bp


@pizzas_bp.route('/')
def index():
    return render_template('pizzas/pizzas.html')


@pizzas_bp.route('/traditional')
def traditional():
    return render_template('pizzas/traditional.html')


@pizzas_bp.route('/artisan')
def artisan():
    return render_template('pizzas/artisan.html')


@pizzas_bp.route('/half')
def half():
    return render_template('pizzas/half.html')


@pizzas_bp.route('/sweet')
def sweet():
    return render_template('pizzas/sweet.html')
