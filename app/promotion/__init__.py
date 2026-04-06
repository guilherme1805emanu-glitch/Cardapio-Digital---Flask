from flask import Blueprint
import os

template_dir = os.path.join(os.path.dirname(__file__), 'templates')

promotion_bp = Blueprint(
    'promotion', __name__,
    template_folder=template_dir,
    static_folder=template_dir,
    static_url_path='/promotion/static'
)

from . import routes
