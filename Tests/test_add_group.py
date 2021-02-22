# -*- coding: utf-8 -*-
from Models.group_class import Group


def test_add_normal_group(app):
    app.group.create(Group(_name="group_1", _header="group_1", _footer="group_1"))


def test_add_empty_group(app):
    app.group.create(Group(_name="", _header="", _footer=""))
