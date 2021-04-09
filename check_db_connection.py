import pymysql.cursors
#from Fixtures.db import DbFixture
from Fixtures.orm import ORMFixture
from Models.group_class import Group

db = ORMFixture(host_value="127.0.0.1", name_value="addressbook", user_value="root", password_value="")

try:
    contact_list = db.get_contacts_in_group(Group(_id="233"))
    for item in contact_list:
        print(item)
    print(len(contact_list))

finally:
    pass




# try:
#     contact_list = db.get_contact_list()
#     for item in contact_list:
#         print(item)
#     print(len(contact_list))
#
# finally:
#     pass



# try:
#     group_list = db.get_group_list()
#     for item in group_list:
#         print(item)
#     print(len(group_list))
#
# finally:
#     pass

# db  = DbFixture(host_value="127.0.0.1", name_value="addressbook", user_value="root", password_value="")
#
# try:
#     groups = db.get_group_list()
#     for group in groups:
#         print(group)
#     print(len(groups))
# finally:
#     db.destroy()

# try:
#     contacts = db.get_contact_list()
#     for contact in contacts:
#         print(contact)
#     print(len(contacts))
#
# finally:
#     db.destroy()
