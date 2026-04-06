from flask import Blueprint
import os

template_dir = os.path.join(os.path.dirname(__file__), 'templates')

categories_bp = Blueprint(
    'categories', __name__,
    template_folder=template_dir,
    static_folder=template_dir,
    static_url_path='/categories/static'
)

from . import routes
