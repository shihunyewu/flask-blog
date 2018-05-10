"""
蓝本中定义程序路由
"""
from datetime import datetime
from flask import render_template, session, redirect, url_for

from . import main
from .forms import NameForm
from .. import db
from ..models import User


@main.route('/', methods=['GET', 'POST'])
def index():
    """
    首页
    :return:
    """
    form = NameForm()
    if form.validate_on_submit():
        session['name'] = form.name.data
        # 每个蓝本都有自己的命名空间
        # 命名空间就是注册蓝本时，main = Blueprint('main', __name__)的第一个参数
        # 用url_for路由的时候，使用 命名空间.路由
        # 命名空间在本文件，可以省略命名空间，直接使用 .路由
        # 视图函数 index() 注册的端点名是 main.index
        return redirect(url_for('main.index'))
    return render_template('index.html', name=form.name.data)


@main.route('/user')
def temp_user():
    """
    暂时查看 user.html 页面
    :return:
    """
    return render_template('user.html')
