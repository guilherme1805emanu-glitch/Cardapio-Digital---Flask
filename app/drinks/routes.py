from flask import render_template
from . import drinks_bp


@drinks_bp.route('/')
def index():
    return render_template('drinks/drinks.html')
