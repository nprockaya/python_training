# -*- coding: utf-8 -*-
from Models.contact_class import Contact

def test_edit_first_contact(app):
    if app.contact.count_contacts() == 0:
        app.contact.create(
            Contact(first_name_value="for_edit_test", middle_name_value="for_edit_test",
                    last_name_value="for_edit_test", nickname_value="for_edit_test",
                    title_value="for_edit_test", company_value="for_edit_test",
                    address_value="for_edit_test", home_phone_value="for_edit_test",
                    mobile_phone_value="for_edit_test", work_phone_value="for_edit_test", fax_value="for_edit_test",
                    email_value="for_edit_test", email2_value="for_edit_test", email3_value="for_edit_test",
                    homepage_value="for_edit_test", bday_value="7", bmonth_value="July",
                    byear_value="2007", aday_value="8", amonth_value="August",
                    ayear_value="2008", secondary_address_value="for_edit_test", secondary_home_value="for_edit_test",
                    secondary_notes_value="for_edit_test"))
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
