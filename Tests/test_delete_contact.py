import random
from Models.contact_class import Contact


def test_delete_some_contact(app, db, check_ui):
    contact = Contact(first_name_value="Firstname", middle_name_value="Middlename", last_name_value="Lastname",
                      nickname_value="Nickname", title_value="Title", company_value="Company",
                      address_value="123456, address_city, address_street, address_home",
                      home_phone_value="123456_home_phone", mobile_phone_value="123456_mobile_phone",
                      work_phone_value="123456_work_phone", fax_value="123456_fax", email_value="1@mail.com",
                      email2_value="2@mail.com", email3_value="3@mail.com", homepage_value="https://home_page.com",
                      bday_value="1", bmonth_value="January", byear_value="2000", aday_value="1",
                      amonth_value="January",
                      ayear_value="2020", secondary_address_value="Second address", secondary_home_value="Second home",
                      secondary_notes_value="Notes")
    if app.contact.count_contacts() == 0:
        app.contact.create(contact)
    old_contacts = db.get_contact_list()
    contact = random.choice(old_contacts)
    # index = randrange(len(old_contacts))
    # app.contact.delete_contact_by_index(index)
    app.contact.delete_contact_by_id(contact.contact_id)
    new_contacts = db.get_contact_list()
    assert len(old_contacts) - 1 == len(new_contacts)
    old_contacts.remove(contact)
    assert old_contacts == new_contacts
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(),
                                                                     key=Contact.id_or_max)
