from Models.group_class import Group
from random import randrange


def test_edit_group_name(app):
    if app.group.count_groups() == 0:
        app.group.create(Group(_name="for_edit_test", _header="", _footer=""))
    old_groups = app.group.get_group_list()
    index = randrange(len(old_groups))
    group = Group(_name="name_group_edit_test")
    group.group_id = old_groups[index].group_id
    app.group.edit_group_by_index(index, group)
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)
    old_groups[index] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
