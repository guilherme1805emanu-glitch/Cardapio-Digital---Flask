from flask import render_template
from . import score_bp


@score_bp.route('/')
def index():
    return render_template('score/score.html')
