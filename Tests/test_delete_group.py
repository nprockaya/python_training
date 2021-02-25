from Models.group_class import Group

def test_delete_first_group(app):
    if app.group.count() == 0:
        app.group.create(Group(_name="for_delete_test", _header="for_delete_test", _footer="for_delete_test"))
    app.group.delete_first_group()
