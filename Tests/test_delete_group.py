from Models.group_class import Group
import random


def test_delete_some_group(app, db):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(_name="for_delete_test", _header="for_delete_test", _footer="for_delete_test"))
    old_groups = db.get_group_list()
    group = random.choice(old_groups)
    # index = randrange(len(old_groups))
    app.group.delete_group_by_id(group.group_id)
    new_groups = db.get_group_list()
    assert len(old_groups) - 1 == len(new_groups)
    old_groups.remove(group)
    # old_groups[index:index + 1] = []
    assert old_groups == new_groups
