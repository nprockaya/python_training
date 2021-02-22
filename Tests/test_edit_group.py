from Models.group_class import Group


# def test_delete_first_group(app):
#     app.session.login(user_name="admin", password="secret")
#     app.group.edit_first_group(
#         Group(_name="name_group_edit_test", _header="header_group_edit_test", _footer="footer_group_edit_test"))
#     app.session.logout()

def test_edit_first_group_name(app):
    app.session.login(user_name="admin", password="secret")
    app.group.edit_first_group(
        Group(_name="name_group_edit_test"))
    app.session.logout()


def test_edit_first_group_header(app):
    app.session.login(user_name="admin", password="secret")
    app.group.edit_first_group(
        Group(_header="header_group_edit_test"))
    app.session.logout()


def test_edit_first_group_footer(app):
    app.session.login(user_name="admin", password="secret")
    app.group.edit_first_group(
        Group(_footer="footer_group_edit_test"))
    app.session.logout()
