from Models.contact_class import Contact
from Models.group_class import Group


def test_delete_contact_from_group(app, db, check_ui):
    contacts_in_groups = db.get_contacts_in_groups_list()
    # If no contact is added to the group
    if len(contacts_in_groups) == 0:
        contacts = db.get_contact_list()
        groups = db.get_group_list()
        if len(contacts) == 0:
            app.contact.create(get_test_contact())
            contact_for_test = db.get_latest_added_contact()
        else:
            contact_for_test = contacts[0]
        if len(groups) == 0:
            app.group.create(get_test_group())
            group_for_test = db.get_latest_added_group()
        else:
            group_for_test = groups[0]
        assert contact_for_test is not None and group_for_test is not None
        # Add contact to group
        app.contact.add_contact_to_group(contact_for_test, group_for_test)
        contact_in_group = db.get_latest_contact_in_group()
        contacts_in_groups_after_add = db.get_contacts_in_groups_list()
        assert len(contacts_in_groups) + 1 == len(contacts_in_groups_after_add)
        contacts_in_groups = contacts_in_groups_after_add
    else:
        contact_in_group = contacts_in_groups[0]

    app.contact.delete_contact_from_group(contact_in_group)

    new_contacts_in_groups_after_add = db.get_contacts_in_groups_list()

    assert len(contacts_in_groups) - 1 == len(new_contacts_in_groups_after_add)
    assert contact_in_group not in new_contacts_in_groups_after_add


def get_test_contact():
    return Contact(first_name_value="Firstname", middle_name_value="Middlename", last_name_value="Lastname",
                   nickname_value="Nickname", title_value="Title", company_value="Company",
                   address_value="123456, address_city, address_street, address_home",
                   home_phone_value="123456_home_phone", mobile_phone_value="123456_mobile_phone",
                   work_phone_value="123456_work_phone", fax_value="123456_fax", email_value="1@mail.com",
                   email2_value="2@mail.com", email3_value="3@mail.com", homepage_value="https://home_page.com",
                   bday_value="1", bmonth_value="January", byear_value="2000", aday_value="1",
                   amonth_value="January",
                   ayear_value="2020", secondary_address_value="Second address", secondary_home_value="Second home",
                   secondary_notes_value="Notes")


def get_test_group():
    return Group(_name="Name", _header="Header", _footer="Footer")
