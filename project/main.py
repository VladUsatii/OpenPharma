#!/usr/bin/env python3
from flask import Flask, Blueprint, render_template
from flask_login import login_required, current_user
from . import db

main = Blueprint('main', __name__)

@main.route('/')
def index():
	return render_template('index.html')

#@main.route('/login/')
#def login(name=None):
	# return render_template('login.html', name=name)

@main.route('/profile')
@login_required
def profile():
	return render_template('profile.html', name=current_user.name)
