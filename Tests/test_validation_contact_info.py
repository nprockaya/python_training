from random import randrange

from Utils.string_utils import clear_spaces_and_hyphens as clear


def test_phones_on_homepage(app):
    contact_list = app.contact.get_contact_list()
    index = randrange(len(contact_list))
    contact_from_home_page = contact_list[index]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(index)
    assert clear(contact_from_home_page.first_name) == clear(contact_from_edit_page.first_name)
    assert clear(contact_from_home_page.last_name) == clear(contact_from_edit_page.last_name)
    assert clear(contact_from_home_page.address) == clear(contact_from_edit_page.address)
    assert clear(contact_from_home_page.all_emails_from_home_page) == clear(
        contact_from_edit_page.merge_emails_like_on_home_page(True))
    assert clear(contact_from_home_page.all_phones_from_home_page) == clear(
        contact_from_edit_page.merge_phones_like_on_home_page())
