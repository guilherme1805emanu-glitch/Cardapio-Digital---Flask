from flask import Blueprint
import os

template_dir = os.path.join(os.path.dirname(__file__), 'templates')

dashboard_bp = Blueprint(
    'dashboard', __name__,
    template_folder=template_dir,
    static_folder=template_dir,
    static_url_path='/dashboard/static'
)

from . import routes
