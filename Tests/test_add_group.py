# -*- coding: utf-8 -*-
from Models.group_class import Group


def test_add_normal_group(appgroup):
    appgroup.session.login(user_name="admin", password="secret")
    appgroup.group.create(Group(_name="group_1", _header="group_1", _footer="group_1"))
    appgroup.session.logout()


def test_add_empty_group(appgroup):
    appgroup.session.login(user_name="admin", password="secret")
    appgroup.group.create(Group(_name="", _header="", _footer=""))
    appgroup.session.logout()