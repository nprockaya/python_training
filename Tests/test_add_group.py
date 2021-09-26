# -*- coding: utf-8 -*-
# from Data.groups_data import constant as test_data_for_group
import allure

from Models.group_class import Group


# @pytest.mark.parametrize("group", test_data_for_group, ids=[repr(x) for x in test_data_for_group])
def test_add_normal_group(app, db, json_groups, check_ui):
    group = json_groups
    with allure.step("Giver a group list"):
        old_groups = db.get_group_list()
    with allure.step("When I add a group %s to the list" % group):
        app.group.create(group)
    with allure.step("Then the new group list is equal to the old list with the added group"):
        new_groups = db.get_group_list()
        old_groups.append(group)
        if check_ui:
            assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
