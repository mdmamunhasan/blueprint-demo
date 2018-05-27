from flask import Flask
from flask_bootstrap import Bootstrap

app = Flask(__name__)
Bootstrap(app)

from project.api.routes import api_index
from project.site.routes import site_index
from project.admin.routes import admin_index

app.register_blueprint(site_index)
app.register_blueprint(api_index, url_prefix='/api')
app.register_blueprint(admin_index, url_prefix='/admin')
