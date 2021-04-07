# -*- coding: utf-8 -*-
from Models.contact_class import Contact
# from Data.contact import test_data_for_contact
# import pytest

# @pytest.mark.parametrize("contact", test_data_for_contact, ids=[repr(x) for x in test_data_for_contact])


def test_add_contact_normal(app, json_contacts):
    contact = json_contacts
    old_contacts = app.contact.get_contact_list()
    app.contact.create(contact)
    assert len(old_contacts) + 1 == app.contact.count_contacts()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
