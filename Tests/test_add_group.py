# -*- coding: utf-8 -*-
from Fixtures.application_for_groups import Application
from Models.group_class import Group
import pytest


@pytest.fixture()
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_normal_group(app):
    app.session.login(user_name="admin", password="secret")
    app.group.create(Group(_name="group_1", _header="group_1", _footer="group_1"))
    app.session.logout()


def test_add_empty_group(app):
    app.session.login(user_name="admin", password="secret")
    app.group.create(Group(_name="", _header="", _footer=""))
    app.session.logout()