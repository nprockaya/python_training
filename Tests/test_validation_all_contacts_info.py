from Models.contact_class import Contact


def test_all_phones_on_homepage(app, db):
    ui_contacts_list = app.contact.get_contact_list()
    db_contacts_list = db.get_contact_list()
    print(sorted(ui_contacts_list, key=Contact.id_or_max))
    print(sorted(db_contacts_list, key=Contact.id_or_max))
    assert sorted(ui_contacts_list, key=Contact.id_or_max) == sorted(db_contacts_list, key=Contact.id_or_max)
