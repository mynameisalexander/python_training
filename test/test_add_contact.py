# -*- coding: utf-8 -*-
import pytest
from model.contact import Contact
from fixture.application import Application


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.general_data(Contact(firstname="qwe", middlename="qwe", lastname="qwe", nickname="qwe",
                                     title="qwe",     company="qwe",    address="qwe",  home="123",
                                     mobile="123",    work="123",       fax="123",      email2="qwe",
                                     email3="qwe",    homepage="qwe",   bday=1,         bmonth=1,
                                     byear=1999,      aday=2,           amonth=2,       ayear=2000,
                                     address2="qwe",  phone2="123",     notes="qwe"))
    app.session.logout()

