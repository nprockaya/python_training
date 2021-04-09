from pony.orm import *
from Models.contact_class import Contact
from Models.group_class import Group
from pymysql.converters import decoders


class ORMFixture:
    db = Database()

    class ORMGroup(db.Entity):
        _table_ = "group_list"
        group_id = PrimaryKey(int, column="group_id")
        name = Optional(str, column="group_name")
        header = Optional(str, column="group_header")
        footer = Optional(str, column="group_footer")
        contacts = Set(lambda: ORMFixture.ORMContact, table="address_in_groups", column="id", reverse="groups",
                       lazy=True)

    class ORMContact(db.Entity):
        _table_ = "addressbook"
        contact_id = PrimaryKey(int, column="id")
        firstname = Optional(str, column="firstname")
        lastname = Optional(str, column="lastname")
        deprecated = Optional(str, column="deprecated")
        groups = Set(lambda: ORMFixture.ORMGroup, table="address_in_groups", column="group_id", reverse="contacts",
                     lazy=True)

    def __init__(self, host_value, name_value, user_value, password_value):
        self.db.bind('mysql', host=host_value, database=name_value, user=user_value, password=password_value) # ,conv=decoders
        self.db.generate_mapping()
        sql_debug(True)

    def convert_groups_to_model(self, groups):
        def convert(group):
            return Group(_id=str(group.group_id), _name=group.name, _header=group.header, _footer=group.footer)

        return list(map(convert, groups))

    def convert_contacts_to_model(self, contacts):
        def convert(contact):
            return Contact(contact_id_value=str(contact.contact_id), first_name_value=contact.firstname,
                           last_name_value=contact.lastname)

        return list(map(convert, contacts))

    @db_session
    def get_group_list(self):
        return self.convert_groups_to_model(select(g for g in ORMFixture.ORMGroup))

    @db_session
    def get_contact_list(self):
        return self.convert_contacts_to_model(select(c for c in ORMFixture.ORMContact if c.deprecated is None))

    @db_session
    def get_contacts_in_group(self, group):
        orm_group = list(select(g for g in ORMFixture.ORMGroup if g.group_id == group.group_id))[0]
        return self.convert_contacts_to_model(orm_group.contacts)
