#-*- coding: utf-8 -*-
from flask import Flask, g, render_template
from flask_sqlalchemy import SQLAlchemy
from flask.ext.login import current_user

app = Flask(__name__)
app.config.from_object('config')

db = SQLAlchemy(app)

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404

@app.before_request
def before_request():
    g.user = current_user

# Import views
import webgui.views.login
import webgui.views.dashboard
