#-*- coding: utf-8 -*-

from flask.ext.login import current_user
from webgui import app
import webgui.models as models

@app.context_processor
def context_templates():
    if current_user.is_authenticated():
        logon = models.User.query.filter_by(
            id=current_user.get_id()
        ).first()
    else:
        logon = None
    return dict(
        username=logon.login if logon else "",
        name=logon.name if logon else ""
    )

