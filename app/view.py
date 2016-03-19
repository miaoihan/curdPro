#!/usr/bin/python
# coding=utf-8
from app import app, db
from flask import render_template, request, url_for, redirect, flash, session
from app.model import Question
from flask_wtf import Form
from wtforms import StringField, SubmitField, TextAreaField, validators, TextField
from wtforms.validators import DataRequired, Length, EqualTo


class QuestionForm(Form):
    # email = StringField('Email', validators=[Required(), Length(1, 64),
    #                     Email()])
    # password = PasswordField('Password', validators=[Required()])
    question = StringField('问题', validators=[DataRequired(message='不能是空的哦'), Length(4, 30, message='长度在4-30之间')])
    author = StringField('作者', validators=[DataRequired()])
    answer = TextAreaField('回答', validators=[DataRequired()])
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
        # question_id = request.form['question_id']
        session['question_id'] = request.form['question_id']
        question_id = session.get('question_id')
        # return '<script>alert("OK!")</script>'
        if question_id is '':
            question = Question(question=form.question.data,
                                author=form.author.data,
                                answer=form.answer.data)
        else:
            question = Question(id=question_id,
                                question=form.question.data,
                                author=form.author.data,
                                answer=form.answer.data)
        db.session.merge(question)
        db.session.commit()
        # flash('保存成功')
        return redirect(url_for('show_question'))
    return render_template('new_question.html', form=form)


@app.route('/edit_question/<question_id>', methods=['GET', 'POST'])
def edit_question(question_id):
    # print(question_id)
    question = Question.query.get_or_404(question_id)
    form = QuestionForm()
    # 设置编辑传过去的值
    form.question.data = question.question
    form.author.data = question.author
    form.answer.data = question.answer
    return render_template('edit_question.html', form=form, question_id=question_id)


@app.route('/del_question/<question_id>')
def del_question(question_id):
    question = Question.query.get_or_404(question_id)
    question.del_status = 0
    db.session.commit()
    return redirect(url_for('show_question'))
