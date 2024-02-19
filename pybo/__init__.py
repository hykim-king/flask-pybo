# Created by user at 2024-02-14
from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

import config

db=SQLAlchemy()
migrate=Migrate()


#애플리케이션 팩토리
def create_app():
    app = Flask(__name__)
    app.config.from_object(config)

    #ORM
    db.init_app(app)
    migrate.init_app(app,db)
    from . import models

    #print(f"__name__:{__name__}")

    #Blueprint등록
    from .views import main_views,question_views,answer_views,auth_views

    app.register_blueprint(main_views.bp)#main
    app.register_blueprint(question_views.bp)#Question
    app.register_blueprint(answer_views.bp)#Answer
    app.register_blueprint(auth_views.bp)

    #필터:datetime으로 등록
    from .filter import formatDateTime
    app.jinja_env.filters['datetime'] = formatDateTime

    return app
    
    



