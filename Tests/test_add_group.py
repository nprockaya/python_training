# -*- coding: utf-8 -*-
from Models.group_class import Group
# from Data.groups_data import constant as test_data_for_group
# import pytest


# @pytest.mark.parametrize("group", test_data_for_group, ids=[repr(x) for x in test_data_for_group])
def test_add_normal_group(app, db, json_groups, check_ui):
    group = json_groups
    old_groups = db.get_group_list()
    app.group.create(group)
    new_groups = db.get_group_list()
    old_groups.append(group)
    if check_ui:
        assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
