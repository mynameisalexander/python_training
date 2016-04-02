# -*- coding: utf-8 -*-
from model.contact import Contact


def test_modify_contact_top(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="test"))
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname="update", middlename="update", lastname="update", nickname="update",
                      title="update",     company="update",    address="update",  home="321",
                      mobile="321",       work="321",          fax="321",         email2="update")
    contact.id = old_contacts[0].id
    app.contact.modify_first_contact(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts[0] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


#def test_modify_contact_bottom(app):
#    old_contacts = app.contact.get_contact_list()
#    app.contact.modify_first_contact(Contact(email3="update",   homepage="update", bday=12,         bmonth=2,
#                                             byear=1988,        aday=9,            amonth=6,        ayear=1945,
#                                             address2="update", phone2="321",      notes="update"))
#    new_contacts = app.contact.get_contact_list()
#    assert len(old_contacts) == len(new_contacts)
