from flask_wtf import Form
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Length


class QuestionForm(Form):
    # email = StringField('Email', validators=[Required(), Length(1, 64),
    #                     Email()])
    # password = PasswordField('Password', validators=[Required()])
    question = StringField('问题', validators=[DataRequired(message='不能是空的哦'), Length(4, 30, message='长度在4-30之间')])
    author = StringField('作者', validators=[DataRequired()])
    answer = TextAreaField('回答', validators=[DataRequired()])
    submit = SubmitField('保存')
