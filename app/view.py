#!/usr/bin/python
# coding=utf-8
from app import app, db
from flask import render_template, request, url_for, redirect, session
from app.model import Question
from flask.ext.wtf import Form
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired


class NameForm(Form):
    question = StringField('问题', validators=[DataRequired()])
    author = StringField('作者')
    content = TextAreaField('内容')
    submit = SubmitField('Submit')


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/questions')
def show_question():
    questions = Question.query.filter_by(del_status=1)
    return render_template('show_question.html', questions=questions)


@app.route('/new_question', methods=['GET','POST'])
def new_question():
    name = None
    form = NameForm()
    if form.validate_on_submit():
        name = form.name.data
        form.name.data = ''
    return render_template('new_question.html', form=form, name=name)
