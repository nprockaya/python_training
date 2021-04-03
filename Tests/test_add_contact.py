# -*- coding: utf-8 -*-
from calendar import January, February

from Models.contact_class import Contact
import random
import string
import pytest


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + " " * 10  # + string.punctuation
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


def random_day():
    day = str(random.randrange(1, 31))
    return day


def random_month():
    months = ["January", "February", "March", "April", "May", "June", "July", "August",
              "September", "October", "November", "December"]
    return random.choice(months)


def random_year():
    year = str(random.randrange(1970, 2021))
    return year


test_data_for_contact = [Contact(first_name_value="", middle_name_value="", last_name_value="",
                                 nickname_value="", title_value="", company_value="",
                                 address_value="",
                                 home_phone_value="", mobile_phone_value="",
                                 work_phone_value="", fax_value="",
                                 email_value="", email2_value="", email3_value="",
                                 homepage_value="",
                                 bday_value="-", bmonth_value="-", byear_value="",
                                 aday_value="-", amonth_value="-", ayear_value="",
                                 secondary_address_value="",
                                 secondary_home_value="",
                                 secondary_notes_value="")] + \
                        [Contact(first_name_value=random_string("first_name", 10),
                                 middle_name_value=random_string("middle_name", 10),
                                 last_name_value=random_string("last_name", 10),
                                 nickname_value=random_string("nickname", 10),
                                 title_value=random_string("title", 20),
                                 company_value=random_string("company_name", 20),
                                 address_value=random_string("address", 40),
                                 home_phone_value=random_string("home_phone", 10),
                                 mobile_phone_value=random_string("mobile_phone", 10),
                                 work_phone_value=random_string("work_phone", 10),
                                 fax_value=random_string("fax", 10),
                                 email_value=random_string("email", 15),
                                 email2_value=random_string("email2", 15),
                                 email3_value=random_string("email3", 15),
                                 homepage_value=random_string("homepage", 20),
                                 bday_value=random_day(), bmonth_value=random_month(), byear_value=random_year(),
                                 aday_value=random_day(), amonth_value=random_month(), ayear_value=random_year(),
                                 secondary_address_value=random_string("secondary_address", 40),
                                 secondary_home_value=random_string("secondary_home", 10),
                                 secondary_notes_value=random_string("secondary_notes", 40)) for i in range(1)]


@pytest.mark.parametrize("contact", test_data_for_contact, ids=[repr(x) for x in test_data_for_contact])
def test_add_contact_normal(app, contact):
    old_contacts = app.contact.get_contact_list()
    old_contacts = app.contact.get_contact_list()
    app.contact.create(contact)
    assert len(old_contacts) + 1 == app.contact.count_contacts()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
