import pymysql

from Models.contact_class import Contact
from Models.contact_in_group_class import ContactInGroup
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

    def get_latest_added_group(self):
        group = None
        cursor = self.connection.cursor()
        try:
            cursor.execute(
                "select group_id, group_name, group_header, group_footer from group_list "
                "where group_id in (select max(group_id))")
            for row in cursor:
                (group_id, name, header, footer) = row
                group = Group(_id=str(group_id), _name=name, _header=header, _footer=footer)
        finally:
            cursor.close()
        return group

    def get_contact_list(self):
        contact_list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute(
                "select id, firstname, lastname, address, email, email2, email3, home, mobile, work, phone2 from "
                "addressbook where deprecated='0000-00-00 00:00:00'")
            for row in cursor:
                (id, firstname, lastname, address, email, email2, email3, home, mobile, work, phone2) = row
                contact_list.append(
                    Contact(contact_id_value=str(id), first_name_value=firstname, last_name_value=lastname,
                            address_value=address, email_value=email, email2_value=email2, email3_value=email3,
                            home_phone_value=home, mobile_phone_value=mobile, work_phone_value=work,
                            secondary_home_value=phone2))
        finally:
            cursor.close()
        return contact_list

    def get_latest_added_contact(self):
        contact = None
        cursor = self.connection.cursor()
        try:
            cursor.execute(
                "select id, firstname, lastname, address, email, email2, email3, home, mobile, work, phone2 from "
                "addressbook where (id in (select max(id))) and (`deprecated`='0000-00-00 00:00:00')")
            for row in cursor:
                (id, firstname, lastname, address, email, email2, email3, home, mobile, work, phone2) = row
                contact = Contact(contact_id_value=str(id), first_name_value=firstname, last_name_value=lastname,
                                  address_value=address, email_value=email, email2_value=email2, email3_value=email3,
                                  home_phone_value=home, mobile_phone_value=mobile, work_phone_value=work,
                                  secondary_home_value=phone2)
        finally:
            cursor.close()
        return contact

    def get_contacts_in_groups_list(self):
        contacts_in_groups_list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute(
                "select id, group_id from address_in_groups")
            for row in cursor:
                (id, group_id) = row
                contacts_in_groups_list.append(ContactInGroup(str(id), str(group_id)))
        finally:
            cursor.close()
        return contacts_in_groups_list

    def get_latest_contact_in_group(self):
        contact_in_group = None
        cursor = self.connection.cursor()
        try:
            cursor.execute(
                "select id, group_id from address_in_groups where created in (select max(created))")
            for row in cursor:
                (id, group_id) = row
                contact_in_group = ContactInGroup(str(id), str(group_id))
        finally:
            cursor.close()
        return contact_in_group

    def destroy(self):
        self.connection.close()
