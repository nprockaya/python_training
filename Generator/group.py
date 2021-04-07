import jsonpickle
import os
import random
import string
from Models.group_class import Group
import getopt
import sys

try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number_of_groups", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

n = 2
f = "data/groups.json"

for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + " " * 10  # + string.punctuation
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


test_data_for_group = [Group(_name="", _header="", _footer="")] + \
                      [Group(_name=random_string("group_name", 10),
                             _header=random_string("group_name", 20),
                             _footer=random_string("group_name", 20)) for i in range(n)]

# test_data_for_group = [Group(_name=name, _header=header, _footer=footer)
#              for name in ["", random_string("group_name", 10)]
#              for header in ["", random_string("group_name", 20)]
#              for footer in ["", random_string("group_name", 20)]]

group_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

with open(group_file, "w") as file:
    # file.write(json.dumps(test_data_for_group, default=lambda x: x.__dict__, indent=2))
    jsonpickle.set_encoder_options("json", indent=2)
    file.write(jsonpickle.encode(test_data_for_group))