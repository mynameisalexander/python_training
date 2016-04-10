# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app):
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname="new",   middlename="new",  lastname="new",    nickname="new",
                      title="new",       company="new",     address="new",     homephone="123",
                      mobilephone="123", workphone="123",   fax="123",         email="new",
                      email2="new",      email3="new",      homepage="new",    bday=1,
                      bmonth=1,          byear=1999,        aday=2,            amonth=2,
                      ayear=2000,        address2="new",    secondphone="123", notes="new")
    app.contact.create(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
