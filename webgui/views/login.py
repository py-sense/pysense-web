#-*- coding: utf-8 -*-

from flask import request, redirect, render_template, url_for, flash
from flask.ext.login import (LoginManager, login_required,
    login_user, logout_user, UserMixin)
from flask.ext.babel import Babel, gettext as _
from hashlib import sha256
from webgui import app
from webgui.forms import FormLogin
import webgui.models as models

babel = Babel(app)

# flask-login - Auth config:
login_manager = LoginManager()
login_manager.setup_app(app)
login_manager.login_view = "login"

class User(UserMixin):
    def __init__(self, name, id, active=True):
        self.name = name
        self.id = id
        self.active = active

    def is_active(self):
        return self.active

@login_manager.user_loader
def load_user(id):
    login = models.User.query.get(int(id))
    return User(login.username, login.id)

login_manager.setup_app(app)


@app.route('/login', methods=['GET', 'POST'])
def login():
    """ Login Page """

    form = FormLogin(request.form)
    if request.method == 'POST':
        if form.validate():
            login_info = models.User.query.filter_by(
                username = request.form['username']
            ).first()
            if login_info:
                if (login_info.password == sha256(request.form['password']).hexdigest()):
                    login_user(User(login_info.username, login_info.id))
                    return redirect(request.args.get("next") or url_for("main"))
                else:
                    flash(_(u"Invalid Password"), "error")
                    return redirect(url_for('login'))
            else:
                flash(_(u"User not exists"), "error")
                return redirect(url_for('login'))
        else:
            flash(_(u"You need fill this field"), "error")
            return redirect(url_for('login'))

    else:
        return render_template('login.html',
            form = form
        )

@app.route('/logout')
@login_required
def logout():
    """ Logout Page (remove session of user) """

    logout_user()
    return redirect('/')
