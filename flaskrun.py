#-*- coding: utf-8 -*-
from webgui import app
from webgui import db

db.create_all()

app.run(host=':::', port=8000, debug=True)
