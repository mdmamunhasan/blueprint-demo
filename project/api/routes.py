from flask import Blueprint, jsonify

api_index = Blueprint('api_index', __name__)


@api_index.route('/hello')
def hello():
    d = {
        "title": "Hello, World!"
    }
    return jsonify(d)
