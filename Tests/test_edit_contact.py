# -*- coding: utf-8 -*-
import random
from Models.contact_class import Contact


def test_edit_contact(app, db, check_ui):
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
    new_contact_data = Contact(first_name_value="Edit_name_test", middle_name_value="Edit_middle_name_test",
                               last_name_value="Edit_last_name_test",
                               nickname_value="edit_nickname_test", title_value="edit_title_test",
                               company_value="edit_company_test",
                               address_value="edit_address_test",
                               home_phone_value="edit_home_phone_test", mobile_phone_value="edit_mobile_phone_test",
                               work_phone_value="edit_work_phone_test", fax_value="edit_fax_test",
                               email_value="edit_email_test",
                               email2_value="edit_email2_test", email3_value="edit_email3_test",
                               homepage_value="edit_homepage_test",
                               bday_value="12", bmonth_value="November", byear_value="2020", aday_value="13",
                               amonth_value="November",
                               ayear_value="2023", secondary_address_value="edit_second_address_test",
                               secondary_home_value="edit_second_home_test",
                               secondary_notes_value="edit_notes_test")
    if app.contact.count_contacts() == 0:
        app.contact.create(contact)
    # получаем список контактов из БД
    old_contacts = db.get_contact_list()
    # выбираем из списка случайный контакт
    contact = random.choice(old_contacts)
    # модифицируем контакт
    app.contact.edit_contact_by_id(contact.contact_id, new_contact_data)
    # получаем новый список контактов
    new_contacts = db.get_contact_list()
    # ищем отредактированный контакт по id
    new_contact = next(x for x in new_contacts if x.contact_id == contact.contact_id)
    # в старом списке удаляем старый контакт
    old_contacts.remove(contact)
    # на его место добавляем новый отредактированный
    old_contacts.append(new_contact)
    # сравниваем длины старого и нового списков
    assert len(old_contacts) == len(new_contacts)
    if check_ui:
        assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
