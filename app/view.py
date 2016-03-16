#!/usr/bin/python
# coding=utf-8
from app import app, db
from flask import render_template, request, url_for, redirect, session
from app.model import Question
from datetime import datetime


@app.route('/')
def home():
    return render_template('index.html')


