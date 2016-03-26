# -*- coding: utf-8 -*-
from model.contact import Contact


def test_modify_contact_top(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="test"))
    app.contact.modify_first_contact(Contact(firstname="update", middlename="update", lastname="update", nickname="update",
                                             title="update",     company="update",    address="update",  home="321",
                                             mobile="321",       work="321",          fax="321",         email2="update"))


def test_modify_contact_bottom(app):
    app.contact.modify_first_contact(Contact(email3="update", homepage="update", bday=12, bmonth=2,
                                             byear=1988, aday=9, amonth=6, ayear=1945,
                                             address2="update", phone2="321", notes="update"))