"""
定义orm对象
"""
from . import db
from werkzeug.security import generate_password_hash, check_password_hash


class Role(db.Model):
    """
    用户角色表
    """
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    users = db.relationship('User', backref='role', lazy='dynamic')

    # backref 向 users 表中添加 role 属性，定义反向关系
    # 定义了 lazy = 'dynamic' 是为了通过 role 查找到用户列表时
    # 禁止自动执行查询，这样在执行查询之前可以添加查询的过滤条件

    def __repr__(self):
        return '<Role %r>' % self.name


class User(db.Model):
    """
    用户表
    """
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True)
    password_hash = db.Column(db.String(128))
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))

    def __repr__(self):
        return '<User %r>' % self.username

    @property
    def password(self):
        raise AttributeError('password is not a readable attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    pass
