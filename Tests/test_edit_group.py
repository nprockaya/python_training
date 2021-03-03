from Models.group_class import Group


def test_edit_first_group_name(app):
    if app.group.count_groups() == 0:
        app.group.create(Group(_name="for_edit_test", _header="", _footer=""))
    old_groups = app.group.get_group_list()
    group = Group(_name="name_group_edit_test")
    group.id = old_groups[0].id
    app.group.edit_first_group(group)
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)
    old_groups[0] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)

# def test_edit_first_group_header(app):
#     if app.group.count_groups() == 0:
#         app.group.create(Group(_name="", _header="for_edit_test", _footer=""))
#     old_groups = app.group.get_group_list()
#     app.group.edit_first_group(
#         Group(_header="header_group_edit_test"))
#     new_groups = app.group.get_group_list()
#     assert len(old_groups) == len(new_groups)
#
#
# def test_edit_first_group_footer(app):
#     if app.group.count_groups() == 0:
#         app.group.create(Group(_name="", _header="", _footer="for_edit_test"))
#     old_groups = app.group.get_group_list()
#     app.group.edit_first_group(
#         Group(_footer="footer_group_edit_test"))
#     new_groups = app.group.get_group_list()
#     assert len(old_groups) == len(new_groups)

    # def test_delete_first_group(app):
    #     app.session.login(user_name="admin", password="secret")
    #     app.group.edit_first_group(
    #         Group(_name="name_group_edit_test", _header="header_group_edit_test", _footer="footer_group_edit_test"))
    #     app.session.logout()