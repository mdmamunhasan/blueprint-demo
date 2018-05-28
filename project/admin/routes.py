from flask import Blueprint, render_template, redirect, url_for, flash

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
        flash('Thanks for registering')
        return redirect(url_for('admin_index.dashboard'))
    return render_template('login.html', title="Login", form=form)
