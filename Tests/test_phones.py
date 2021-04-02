def test_phones_on_homepage(app):
    contact_from_home_page = app.contact.get_contact_list()[0]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert contact_from_home_page.home_phone == contact_from_edit_page.home_phone
    assert contact_from_home_page.work_phone == contact_from_edit_page.work_phone
    assert contact_from_home_page.mobile_phone == contact_from_edit_page.mobile_phone
    assert contact_from_home_page.secondary_home == contact_from_edit_page.secondary_home
