from flask import Blueprint, render_template, request, session, redirect, url_for, flash
from project.admin.models import check_user

admin_index = Blueprint('admin_index', __name__, template_folder='templates')

from project.admin.forms import LoginForm


@admin_index.route('/')
def dashboard():
    return render_template('dashboard.html', title="Dashboard")


@admin_index.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        # Todo database and session management
        email = request.form['email']
        password = request.form['password']

        flash('Thanks for registering')
        if check_user(email, password):
            flash('Thanks for registering')
            session['email'] = request.form['email']
            return redirect(url_for('admin_index.dashboard'))

    return render_template('login.html', title="Login", form=form)
