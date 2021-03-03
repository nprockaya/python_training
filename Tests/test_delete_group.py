from Models.group_class import Group


def test_delete_first_group(app):
    if app.group.count_groups() == 0:
        app.group.create(Group(_name="for_delete_test", _header="for_delete_test", _footer="for_delete_test"))
    old_groups = app.group.get_group_list()
    app.group.delete_first_group()
    new_groups = app.group.get_group_list()
    assert len(old_groups) - 1 == len(new_groups)
    old_groups[0:1] = []
    assert len(old_groups) == len(new_groups)
