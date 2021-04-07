import random
import string
from Models.group_class import Group

test_data = [
    Group(_name="name_constant", _header="header_constant", _footer="footer_constant"),
    Group(_name="name_constant_2", _header="header_constant_2", _footer="footer_constant_2")
]

# def random_string(prefix, maxlen):
#     symbols = string.ascii_letters + string.digits + " " * 10  # + string.punctuation
#     return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])
#
#
# test_data_for_group = [Group(_name="", _header="", _footer="")] + \
#                       [Group(_name=random_string("group_name", 10),
#                              _header=random_string("group_name", 20),
#                              _footer=random_string("group_name", 20)) for i in range(1)]

# test_data_for_group = [Group(_name=name, _header=header, _footer=footer)
#              for name in ["", random_string("group_name", 10)]
#              for header in ["", random_string("group_name", 20)]
#              for footer in ["", random_string("group_name", 20)]]

