from flask import Blueprint, render_template, request, redirect, url_for, flash, session, g

site_index = Blueprint('site_index', __name__, template_folder='templates', static_folder='static')

from project.site.models import create_user
from project.site.forms import RegistrationForm


@site_index.before_request
def before_request():
    g.user = None
    if 'user' in session:
        g.user = session['user']


@site_index.route('/')
def home():
    return render_template('home.html', title="Home")


@site_index.route('/register', methods=['GET', 'POST'])
def register():
    if g.user:
        return redirect(url_for('admin_index.dashboard'))

    form = RegistrationForm()
    if form.validate_on_submit():
        email = request.form['email']
        password = request.form['password']
        if create_user(email, password):
            flash('Thanks for registering')
            return redirect(url_for('site_index.home'))

    return render_template('register.html', title="Register", form=form)
