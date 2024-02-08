# Created by user at 2024-02-08



from flask import Blueprint

bp = Blueprint('main', __name__, url_prefix='/')

@bp.route('/hello')
def hello():
    return f'Hello, World!'


@bp.route('/')
def index():
    return f'Index'