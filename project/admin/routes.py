from flask import Blueprint, render_template, redirect, url_for

admin_index = Blueprint('admin_index', __name__, template_folder='templates')


@admin_index.route('/')
def dashboard():
    return render_template('dashboard.html', title="Dashboard")


@admin_index.route('/login')
def login():
    return redirect(url_for('admin_index.dashboard'))
