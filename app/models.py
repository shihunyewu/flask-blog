"""
定义orm对象
"""
from . import db
from werkzeug.security import generate_password_hash,check_password_hash

class Role:
    """
    用户角色表
    """
    pass


class User:
    """
    用户表
    """
    password_hash = db.Column(db.String(128))

    @property
    def password(self):
        raise AttributeError('password is not a readable attribute')

    @password.setter
    def password(self,password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self,password):
        return check_password_hash(self.password_hash,password)

    pass
