"""
程序包用来保存程序的所有代码、模板和静态文件

使用程序工厂函数，一种设计模式
"""

from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_mail import Mail
from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy
from config import config

bootstrap = Bootstrap()
mail = Mail()
moment = Moment()
db = SQLAlchemy()


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    bootstrap.init_app(app)
    mail.init_app(app)
    moment.init_app(app)
    db.init_app(app)

    # 路由和错误处理
    from .main import main as main_blueprint
    # 将蓝本注册到程序上
    app.register_blueprint(main_blueprint)

    return app
