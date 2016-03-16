# encoding=utf8
from datetime import datetime

from . import db


class Question(db.Model):
    # 如果没有定义 __tablename__ ,Flask-
    # 数据库 | 47SQLAlchemy 会使用一个默认名字,但默认的表名没有遵守使用复数形式进行命名的约定

    __tablename__ = 'questions'

    # primary_key 如果设为 True ,这列就是表的主键
    # unique 如果设为 True ,这列不允许出现重复的值
    # index 如果设为 True ,为这列创建索引,提升查询效率
    # nullable 如果设为 True ,这列允许使用空值;如果设为 False ,这列不允许使用空值
    # default 为这列定义默认值
    id = db.Column(db.Integer, primary_key=True, unique=True)
    question = db.Column(db.String(80), nullable=False)
    author = db.Column(db.String(20), nullable=False)
    answer = db.Column(db.String(400), nullable=False)

    del_status = db.Column(db.Integer, default=1)
    created_time = db.Column(db.DateTime, default=datetime.now())

    # def __init__(self, title, author, content, del_status):
    #     self.title = title
    #     self.author = author
    #     self.content = content
    #     self.del_status = del_status

    def __repr__(self):
        id = self.id
        ti = self.title
        return '<id: %d title: %r>' % (self.id, self.question)
