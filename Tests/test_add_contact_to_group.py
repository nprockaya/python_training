from Models.contact_class import Contact
from Models.contact_in_group_class import ContactInGroup
from Models.group_class import Group


def test_add_contact_to_group(app, db, check_ui):
    contact_for_test = None
    group_for_test = None
    contacts_in_groups = db.get_contacts_in_groups_list()
    for contact in db.get_contact_list():
        for group in db.get_group_list():
            # If some contact doesn't added to some group
            if ContactInGroup(contact.contact_id, group.group_id) not in contacts_in_groups:
                contact_for_test = contact
                group_for_test = group

    # If all contacts have been added to all group
    if contact_for_test is None and group_for_test is None:
        app.contact.create(get_test_contact())
        app.group.create(get_test_group())
        contact_for_test = db.get_latest_added_contact()
        group_for_test = db.get_latest_added_group()

    assert contact_for_test is not None and group_for_test is not None

    app.contact.add_contact_to_group(contact_for_test, group_for_test)

    new_contacts_in_groups = db.get_contacts_in_groups_list()

    assert len(contacts_in_groups) + 1 == len(new_contacts_in_groups)
    assert ContactInGroup(contact_for_test.contact_id, group_for_test.group_id) in new_contacts_in_groups


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
