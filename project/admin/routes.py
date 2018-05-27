from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound

admin_index = Blueprint('admin_index', __name__, template_folder='templates')


@admin_index.route('/')
def hello():
    return 'Hello, World!'
