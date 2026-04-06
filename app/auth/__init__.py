from flask import Blueprint
import os

template_dir = os.path.join(os.path.dirname(__file__), 'templates')

auth_bp = Blueprint(
    'auth', __name__,
    template_folder=template_dir,
    static_folder=template_dir,
    static_url_path='/auth/static'
)

from . import routes
