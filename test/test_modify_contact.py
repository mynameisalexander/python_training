# -*- coding: utf-8 -*-
from model.contact import Contact
import random


def test_modify_some_contact(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="test"))
    old_contacts = db.get_contact_list()
    random_contact = random.choice(old_contacts)
    contact = Contact(firstname="update", middlename="update", lastname="update", nickname="update",
                      title="update",     company="update",    address="update",  homephone="321",
                      mobilephone="321",  workphone="321",     fax="321",         email="update")
    contact.id = random_contact.id
    app.contact.modify_contact_by_id(contact)
    new_contacts = db.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    i = 0
    for x in old_contacts:
        if x.id == random_contact.id:
            old_contacts[i] = contact
        i += 1
    assert old_contacts == new_contacts
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)


#def test_modify_contact_bottom(app):
#    old_contacts = app.contact.get_contact_list()
#    app.contact.modify_first_contact(Contact(email3="update",   homepage="update", bday=12,         bmonth=2,
#                                             byear=1988,        aday=9,            amonth=6,        ayear=1945,
#                                             address2="update", phone2="321",      notes="update"))
#    new_contacts = app.contact.get_contact_list()
#    assert len(old_contacts) == len(new_contacts)
