# -*- coding: utf-8 -*-
from Models.group_class import Group
import random
import string
import pytest


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + " " * 10 #+ string.punctuation
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


test_data_for_group = [Group(_name="", _header="", _footer="")] + \
            [Group(_name=random_string("group_name", 10),
                   _header=random_string("group_name", 20),
                   _footer=random_string("group_name", 20)) for i in range(1)]

# test_data_for_group = [Group(_name=name, _header=header, _footer=footer)
#              for name in ["", random_string("group_name", 10)]
#              for header in ["", random_string("group_name", 20)]
#              for footer in ["", random_string("group_name", 20)]]


@pytest.mark.parametrize("group", test_data_for_group, ids=[repr(x) for x in test_data_for_group])
def test_add_normal_group(app, group):
    old_groups = app.group.get_group_list()
    app.group.create(group)
    assert len(old_groups) + 1 == app.group.count_groups()
    new_groups = app.group.get_group_list()
    old_groups.append(group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)