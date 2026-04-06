from flask import Blueprint
import os

template_dir = os.path.join(os.path.dirname(__file__), 'templates')

home_bp = Blueprint(
    'home', __name__,
    template_folder=template_dir,
    static_folder=template_dir,
    static_url_path='/home/static'
)

from . import routes
