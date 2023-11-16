# -*- coding: utf-8 -*-
from model.group import Group


def test_add_group(app):
    app.group.create(Group(name="qwerty", header="3", footer="3"))


def test_add_empty_group(app):
    app.group.create(Group(name="", header="", footer=""))
