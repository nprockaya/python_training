def test_delete_first_contact(app):
    app.session.login(user_name="admin", password="secret")
    app.contact.delete_first_contact()
    app.session.logout()
