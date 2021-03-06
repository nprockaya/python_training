import pymysql

from Models.contact_class import Contact
from Models.group_class import Group


class DbFixture:
    def __init__(self, host_value, name_value, user_value, password_value):
        self.host = host_value
        self.name = name_value
        self.user = user_value
        self.password = password_value
        self.connection = pymysql.connect(host=host_value, database=name_value, user=user_value,
                                          password=password_value, autocommit=True)

    def get_group_list(self):
        group_list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select group_id, group_name, group_header, group_footer from group_list")
            for row in cursor:
                (group_id, name, header, footer) = row
                group_list.append(Group(_id=str(group_id), _name=name, _header=header, _footer=footer))
        finally:
            cursor.close()
        return group_list

    def get_contact_list(self):
        contact_list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select id, firstname, lastname from addressbook where deprecated='0000-00-00 00:00:00'")
            for row in cursor:
                (contact_id, firstname, lastname) = row
                contact_list.append(Contact(contact_id_value=str(contact_id), first_name_value=firstname, last_name_value=lastname))
        finally:
            cursor.close()
        return contact_list

    def destroy(self):
        self.connection.close()
