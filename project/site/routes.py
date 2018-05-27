from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound

site_index = Blueprint('site_index', __name__, template_folder='templates')


@site_index.route('/')
def hello():
    return 'Hello, World!'
