# -*- coding: utf-8 -*-
from model.contact import Contact
from random import randrange


def test_modify_some_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="test"))
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    contact = Contact(firstname="update", middlename="update", lastname="update", nickname="update",
                      title="update",     company="update",    address="update",  homephone="321",
                      mobilephone="321",  workphone="321",     fax="321",         email="update")
    contact.id = old_contacts[index].id
    app.contact.modify_contact_by_id(contact)
    assert len(old_contacts) == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts[index] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


#def test_modify_contact_bottom(app):
#    old_contacts = app.contact.get_contact_list()
#    app.contact.modify_first_contact(Contact(email3="update",   homepage="update", bday=12,         bmonth=2,
#                                             byear=1988,        aday=9,            amonth=6,        ayear=1945,
#                                             address2="update", phone2="321",      notes="update"))
#    new_contacts = app.contact.get_contact_list()
#    assert len(old_contacts) == len(new_contacts)
