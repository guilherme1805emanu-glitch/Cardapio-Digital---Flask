from flask import Blueprint
import os

template_dir = os.path.join(os.path.dirname(__file__), 'templates')

pizzas_bp = Blueprint(
    'pizzas', __name__,
    template_folder=template_dir,
    static_folder=template_dir,
    static_url_path='/pizzas/static'
)

from . import routes
