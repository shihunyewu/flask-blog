"""
单元测试
setUp() 在测试前运行
tearDown() 在测试结束后运行
名字以 test_ 开头的函数都作为测试执行
"""
import unittest
from flask import current_app
from app import create_app, db


class BasicsTestCase(unittest.TestCase):
    def setUp(self):
        """
        尝试创建一个测试环境
        :return:
        """
        self.app = create_app('testing')
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()

    def tearDown(self):
        """
        关闭数据库和所有的上下文
        :return:
        """
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_app_exits(self):
        """
        检测程序实例存在
        :return:
        """
        self.assertFalse(current_app is None)

    def test_app_is_testing(self):
        """
        确保测试在测试配置中运行
        :return:
        """
        self.assertFalse(current_app.config['TESTING'])

