from flask import Blueprint, render_template, request, session, redirect, url_for, flash
from project.admin.models import check_user

admin_index = Blueprint('admin_index', __name__, template_folder='templates')

from project.admin.forms import LoginForm


@admin_index.route('/')
def dashboard():
    if 'email' not in session:
        return redirect(url_for('admin_index.login'))
    return render_template('dashboard.html', title="Dashboard")


@admin_index.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        email = request.form['email']
        password = request.form['password']

        flash('Thanks for registering')
        if check_user(email, password):
            flash('Thanks for registering')
            session['email'] = request.form['email']
            return redirect(url_for('admin_index.dashboard'))

    if 'email' in session:
        return redirect(url_for('admin_index.dashboard'))
    else:
        return render_template('login.html', title="Login", form=form)


@admin_index.route('/logout', methods=['GET'])
def logout():
    session.pop('email', None)
    return redirect(url_for('admin_index.login'))
