import re


def test_phones_on_homepage(app):
    contact_from_home_page = app.contact.get_contact_list()[0]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert contact_from_home_page.all_phones_from_home_page == merge_phones_like_on_home_page(contact_from_edit_page)


def test_phones_on_contact_view_page(app):
    contact_from_view_page = app.contact.get_contact_info_from_view_page(0)
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert contact_from_view_page.home_phone == contact_from_view_page.home_phone
    assert contact_from_view_page.work_phone == contact_from_view_page.work_phone
    assert contact_from_view_page.mobile_phone == contact_from_view_page.mobile_phone
    assert contact_from_view_page.secondary_home == contact_from_view_page.secondary_home


def clear(phone_string):
    return re.sub("[()-]", "", phone_string)


def merge_phones_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                             map(lambda x: clear(x),
                                 filter(lambda x: x is not None,
                                        [contact.home_phone, contact.mobile_phone,
                                         contact.work_phone, contact.secondary_home]))))
