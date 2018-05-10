"""
用于启动改程序以及其他的程序任务
migrate 的主要作用？
"""

import os
from app import create_app, db
from app.models import User, Role
from flask_script import Manager, Shell
from flask_migrate import Migrate, MigrateCommand

app = create_app(os.getenv('FLASK_CONFIG') or 'default')
manager = Manager(app)
migrate = Migrate(app, db)


def make_shell_context():
    """
    注册了程序、数据库实例以及模型，这些对象能够直接导入 shell
    :return:
    """
    return dict(app=app, db=db, User=User, Role=Role)


# manager.command 修饰器让自定义命令变得简单
# 修饰函数名就是命令名
@manager.command
def test():
    """
    启动测试脚本
    :return:
    """
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)


# 将这些对象导入到 shell
manager.add_command('shell', Shell(make_context=make_shell_context))
# 导入 migrate 命令，用来迁移数据库
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()
