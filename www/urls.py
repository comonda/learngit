# !/usr/bin/env python
# -*- coding: utf-8 -*_

__author__ = 'comon'

import logging

from transwarp.web import get, view

from models import User, Comment, Blog

@view('test_users.html')
@get('/')
def test_users():
    users = User.find_all()
    return dict(users=users)
