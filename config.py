#-*- coding: utf-8 -*-
import os

BASEDIR = os.path.abspath(os.path.dirname(__file__))
DEBUG = False
SECRET_KEY = 'niuksm7nh235hybh786f67vtbnmzkclso/'
PATH_DB = os.path.join(BASEDIR, "db")
SQLALCHEMY_DATABASE_URI = 'sqlite:///%s/pysense.db' % (
    PATH_DB
)
