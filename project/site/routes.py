from flask import Blueprint, render_template, request, redirect, url_for, flash

site_index = Blueprint('site_index', __name__, template_folder='templates')

from project.site.models import create_user
from project.site.forms import RegistrationForm

@site_index.route('/')
def home():
    return render_template('home.html', title="Home")


@site_index.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    email = request.form['email']
    password = request.form['password']
    if create_user(email, password):
        flash('Thanks for registering')
        return redirect(url_for('site_index.home'))
    return render_template('register.html', title="Register", form=form)
