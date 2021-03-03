# -*- coding: utf-8 -*-
from Models.group_class import Group
from sys import maxsize


def test_add_normal_group(app):
    old_groups = app.group.get_group_list()
    group = Group(_name="group_1", _header="group_1", _footer="group_1")
    app.group.create(group)
    new_groups = app.group.get_group_list()
    assert len(old_groups) + 1 == len(new_groups)
    old_groups.append(group)

    def id_or_max(gr):
        if gr.id:
            return int(gr.id)
        else:
            return maxsize
    assert sorted(old_groups, key=id_or_max) == sorted(new_groups, key=id_or_max)

# def test_add_empty_group(app):
#     old_groups = app.group.get_group_list()
#     app.group.create(Group(_name="", _header="", _footer=""))
#     new_groups = app.group.get_group_list()
#     assert len(old_groups) + 1 == len(new_groups)