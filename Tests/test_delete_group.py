def test_delete_first_group(appgroup):
    appgroup.session.login(user_name="admin", password="secret")
    appgroup.group.delete_first_group()
    appgroup.session.logout()
