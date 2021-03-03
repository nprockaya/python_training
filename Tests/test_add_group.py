# -*- coding: utf-8 -*-
from Models.group_class import Group


def test_add_normal_group(app):
    old_groups = app.group.get_group_list()
    app.group.create(Group(_name="group_1", _header="group_1", _footer="group_1"))
    new_groups = app.group.get_group_list()
    assert len(old_groups) + 1 == len(new_groups)


def test_add_empty_group(app):
    old_groups = app.group.get_group_list()
    app.group.create(Group(_name="", _header="", _footer=""))
    new_groups = app.group.get_group_list()
    assert len(old_groups) + 1 == len(new_groups)