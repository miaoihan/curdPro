#!/usr/bin/python
# coding=utf-8
from app import app, db
from flask import render_template, request, url_for, redirect, flash
from app.model import Question
from flask.ext.wtf import Form
from wtforms import StringField, SubmitField, TextAreaField, validators
from wtforms.validators import DataRequired


class QuestionForm(Form):
    question = StringField('问题', validators=[DataRequired()])
    author = StringField('作者')
    answer = TextAreaField('回答')
    submit = SubmitField('保存')


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/questions')
def show_question():
    questions = Question.query.filter_by(del_status=1)
    return render_template('show_question.html', questions=questions)


@app.route('/new_question', methods=['GET', 'POST'])
def new_question():
    form = QuestionForm()
    if form.validate_on_submit():
        question = Question(question=form.question, author=form.author, answer=form.answer)
        db.session.add(question)
        db.session.commit()
        flash('保存成功')
        return redirect(url_for('show_question'))
    return render_template('new_question.html', form=form)
