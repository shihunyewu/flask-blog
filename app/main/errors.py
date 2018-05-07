"""
在蓝本中编写错误处理程序稍有不同
如果仍使用 errorhandler修饰器
则只有本蓝本中的错误才能触发。
如果想要处理全局的错误，要用 app_erorhandler
"""
from flask import render_template
from . import main


@main.app_errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@main.app_errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500
