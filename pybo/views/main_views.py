# Created by user at 2024-02-14

from flask import Blueprint

#__name__: main_views.py
bp = Blueprint('main',__name__,url_prefix='/')

@bp.route('/hello')
def hello_pybo():
    return "Hello, world!!!"


@bp.route('/')
def index():
    return '<p> Index </p>'


