from flask import render_template
from . import promotion_bp


@promotion_bp.route('/')
def index():
    return render_template('promotion/promotion.html')
