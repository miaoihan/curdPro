#!/usr/bin/python
# coding=utf-8
from app import app, db
from flask import render_template, request, url_for, redirect, session
from app.model import Question
from datetime import datetime


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/questions')
def show_question():
    questions = Question.query.filter_by(del_status=1)
    return render_template('show_question.html', questions=questions)

