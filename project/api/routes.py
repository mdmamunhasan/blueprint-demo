from flask import Blueprint, jsonify
from project.api.models import get_users

api_index = Blueprint('api_index', __name__)


@api_index.route('/users')
def users():
    d = get_users()
    return jsonify(d)
