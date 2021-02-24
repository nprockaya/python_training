# -*- coding: utf-8 -*-
from Models.contact_class import Contact


def test_edit_first_contact(app):
    app.contact.edit_first_contact(
        Contact(first_name_value="Edit_name_test", middle_name_value="Edit_middle_name_test",
                last_name_value="Edit_last_name_test",
                nickname_value="edit_nickname_test", title_value="edit_title_test", company_value="edit_company_test",
                address_value="edit_address_test",
                home_phone_value="edit_home_phone_test", mobile_phone_value="edit_mobile_phone_test",
                work_phone_value="edit_work_phone_test", fax_value="edit_fax_test", email_value="edit_email_test",
                email2_value="edit_email2_test", email3_value="edit_email3_test", homepage_value="edit_homepage_test",
                bday_value="12", bmonth_value="November", byear_value="2020", aday_value="13", amonth_value="November",
                ayear_value="2023", secondary_address_value="edit_second_address_test",
                secondary_home_value="edit_second_home_test",
                secondary_notes_value="edit_notes_test"))
