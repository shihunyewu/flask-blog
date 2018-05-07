"""
定义 post 表单
"""
from flask_wtf import Form
from wtforms import StringField, SubmitField, validators
from wtforms.validators import Required


class NameForm(Form):
    """
    定义名字表单
    """
    # 这里的 required 需要写成 required()
    name = StringField('What is your name?', validators=[Required()])
    submit = SubmitField('Submit')
    pass
