from Models.contact_class import Contact


def test_delete_first_contact(app):
    if app.contact.count_contacts() == 0:
        app.contact.create(
            Contact(first_name_value="for_delete_test", middle_name_value="for_delete_test",
                    last_name_value="for_delete_test", nickname_value="for_delete_test",
                    title_value="for_delete_test", company_value="for_delete_test",
                    address_value="for_delete_test", home_phone_value="for_delete_test",
                    mobile_phone_value="for_delete_test", work_phone_value="for_delete_test", fax_value="for_delete_test",
                    email_value="for_delete_test", email2_value="for_delete_test", email3_value="for_delete_test",
                    homepage_value="for_delete_test", bday_value="5", bmonth_value="May",
                    byear_value="2005", aday_value="6", amonth_value="June",
                    ayear_value="2006", secondary_address_value="for_delete_test", secondary_home_value="for_delete_test",
                    secondary_notes_value="for_delete_test"))
    app.contact.delete_first_contact()
