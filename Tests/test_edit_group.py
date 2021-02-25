from Models.group_class import Group


# def test_delete_first_group(app):
#     app.session.login(user_name="admin", password="secret")
#     app.group.edit_first_group(
#         Group(_name="name_group_edit_test", _header="header_group_edit_test", _footer="footer_group_edit_test"))
#     app.session.logout()

def test_edit_first_group_name(app):
    if app.group.count_groups() == 0:
        app.group.create(Group(_name="for_edit_test", _header="", _footer=""))
    app.group.edit_first_group(
        Group(_name="name_group_edit_test"))


def test_edit_first_group_header(app):
    if app.group.count_groups() == 0:
        app.group.create(Group(_name="", _header="for_edit_test", _footer=""))
    app.group.edit_first_group(
        Group(_header="header_group_edit_test"))


def test_edit_first_group_footer(app):
    if app.group.count_groups() == 0:
        app.group.create(Group(_name="", _header="", _footer="for_edit_test"))
    app.group.edit_first_group(
        Group(_footer="footer_group_edit_test"))
