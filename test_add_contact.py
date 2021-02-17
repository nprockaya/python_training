# -*- coding: utf-8 -*-
from application_for_contacts import app_for_contacts
from contact_class import Contact
import pytest


@pytest.fixture()
def app(request):
    fixture = app_for_contacts()
    request.addfinilizer(fixture.destroy())
    return fixture


@pytest.fixture()
def app(request):
    fixture = app_for_contacts()
    request.addfinilizer(fixture.destroy())
    return fixture


def test_add_contact_normal(app):
    app.login(user_name="admin", password="secret")
    app.contact_creation(
        Contact(first_name_value="Firstname", middle_name_value="Middlename", last_name_value="Lastname",
                nickname_value="Nickname", title_value="Title", company_value="Company",
                address_value="123456, address_city, address_street, address_home",
                home_phone_value="123456_home_phone", mobile_phone_value="123456_mobile_phone",
                work_phone_value="123456_work_phone", fax_value="123456_fax", email_value="1@mail.com",
                email2_value="2@mail.com", email3_value="3@mail.com", homepage_value="https://home_page.com",
                bday_value="1", bmonth_value="January", byear_value="2000", aday_value="1", amonth_value="January",
                ayear_value="2020", secondary_address_value="Second address", secondary_home_value="Second home",
                secondary_notes_value="Notes"))
    app.logout()


def test_add_contact_empty(app):
    app.login(user_name="admin", password="secret")
    app.contact_creation(
        Contact(first_name_value="", middle_name_value="", last_name_value="",
                nickname_value="", title_value="", company_value="",
                address_value="",
                home_phone_value="", mobile_phone_value="",
                work_phone_value="", fax_value="", email_value="",
                email2_value="", email3_value="", homepage_value="",
                bday_value="", bmonth_value="", byear_value="", aday_value="", amonth_value="",
                ayear_value="", secondary_address_value="", secondary_home_value="",
                secondary_notes_value=""))
    app.logout()