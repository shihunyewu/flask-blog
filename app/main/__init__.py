"""
采用程序工厂函数操作让定义路由变复杂了
在单脚本程序中，程序实例存在于全局作用域中，路由可以直接用 app.route 修饰器定义
使用程序工厂函数，只有调用 create_app() 之后才能使用 app.route

Flask 使用蓝本提供了解决方法
蓝本可以定义路由，但是路由处于休眠状态
当蓝本注册到程序上，路由成为程序的一部分
使用全局作用域中的蓝本时，定义路由的方法几乎和单脚本程序一样
"""

from flask import Blueprint


# 通过实例化一个 Blueprint 类 可以创建蓝本
# 构造函数有两个参数
# 参数1：蓝本的名字
# 参数2：python的 __name__ 变量
main = Blueprint('main', __name__)

# 在脚本的末尾导入，是为了避免循环的导入依赖
# 因为在 views.py 和 erros.py 中还要导入蓝本 main？
from . import views, errors
