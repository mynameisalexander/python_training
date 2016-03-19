# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.create(Contact(firstname="new", middlename="new", lastname="new", nickname="new",
                               title="new", company="new", address="new", home="123",
                               mobile="123", work="123", fax="123", email2="new",
                               email3="new", homepage="new", bday=1, bmonth=1,
                               byear=1999, aday=2, amonth=2, ayear=2000,
                               address2="new", phone2="123", notes="new"))
    app.session.logout()

