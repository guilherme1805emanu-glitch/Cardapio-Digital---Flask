from flask import Blueprint
import os

template_dir = os.path.join(os.path.dirname(__file__), 'templates')

drinks_bp = Blueprint(
    'drinks', __name__,
    template_folder=template_dir,
    static_folder=template_dir,
    static_url_path='/drinks/static'
)

from . import routes
