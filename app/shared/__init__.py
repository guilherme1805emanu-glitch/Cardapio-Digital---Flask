from flask import Blueprint
import os

template_dir = os.path.join(os.path.dirname(__file__), 'templates')

shared_bp = Blueprint(
    'shared', __name__,
    template_folder=template_dir,
    static_folder=template_dir,
    static_url_path='/shared/static'
)
