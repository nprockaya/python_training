from Utils.string_utils import clear_spaces as clear


def test_validation_all_contacts_info(app, db):
    ui_contacts_list = app.contact.get_contact_list()
    db_contacts_list = db.get_contact_list()
    assert len(ui_contacts_list) == len(db_contacts_list)
    for ui_contact in ui_contacts_list:
        db_contact = next(filter(lambda x: x.contact_id == ui_contact.contact_id, db_contacts_list), None)
        assert db_contact is not None
        assert clear(ui_contact.first_name) == clear(db_contact.first_name)
        assert clear(ui_contact.last_name) == clear(db_contact.last_name)
        assert clear(ui_contact.address) == clear(db_contact.address)
        assert clear(ui_contact.all_emails_from_home_page) == clear(db_contact.merge_emails_like_on_home_page(False))
        assert clear(ui_contact.all_phones_from_home_page) == clear(db_contact.merge_phones_like_on_home_page())
