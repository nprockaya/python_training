# -*- coding: utf-8 -*-
from Models.group_class import Group
# from Data.groups_data import constant as test_data_for_group
# import pytest


# @pytest.mark.parametrize("group", test_data_for_group, ids=[repr(x) for x in test_data_for_group])
def test_add_normal_group(app, json_groups):
    group = json_groups
    old_groups = app.group.get_group_list()
    app.group.create(group)
    assert len(old_groups) + 1 == app.group.count_groups()
    new_groups = app.group.get_group_list()
    old_groups.append(group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
