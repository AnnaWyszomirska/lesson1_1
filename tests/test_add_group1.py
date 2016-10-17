# -*- coding: utf-8 -*-
from model.group import Group

def test_add_group(app):
    app.group.create(Group(name="grupa lesson1", header="grupa lesson1", footer="grupa lesson1"))

def test_add_empty_group(app):
    app.group.create(Group(name="", header="", footer=""))
