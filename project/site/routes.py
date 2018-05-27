from flask import Blueprint, render_template

site_index = Blueprint('site_index', __name__, template_folder='templates')


@site_index.route('/')
def home():
    return render_template('home.html', title="Home")

@site_index.route('/register')
def register():
    return render_template('register.html', title="Register")