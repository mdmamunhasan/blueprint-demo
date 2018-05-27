from flask import Blueprint, render_template

admin_index = Blueprint('admin_index', __name__, template_folder='templates')


@admin_index.route('/')
def dashboard():
    return render_template('dashboard.html', title="Dashboard")
