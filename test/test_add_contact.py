# -*- coding: utf-8 -*-
from model.contact import Contact
from random import *
import pytest
import string


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + " "*10
    return prefix + "".join([choice(symbols) for i in range(randrange(maxlen))])


testdata = [
    Contact(firstname="",   middlename="",  lastname="",    nickname="",
            title="",       company="",     address="",     homephone="",
            mobilephone="", workphone="",   fax="",         email="",
            email2="",      email3="",      homepage="",    bday=None,
            bmonth=None,    byear=None,     aday=None,      amonth=None,
            ayear=None,     address2="",    secondphone="", notes="")] + [
    Contact(firstname=random_string("firstname", 10),     middlename=random_string("middlenam", 10),
            lastname=random_string("lastname", 10),       nickname=random_string("nickname", 10),
            title=random_string("title", 10),             company=random_string("company", 10),
            address=random_string("address", 20),         homephone=random_string("homephone", 10),
            mobilephone=random_string("mobilephone", 10), workphone=random_string("workphone", 10),
            fax=random_string("fax", 10),                 email=random_string("workphone", 10),
            email2=random_string("email2", 10),           email3=random_string("email3", 10),
            homepage=random_string("homepage", 10),       address2=random_string("address2", 20),
            secondphone=random_string("secondphone", 20), notes=random_string("notes", 20),
            bday=randrange(3,33), bmonth=randrange(2,13), byear=randrange(1900,2016),
            aday=randrange(3,33), amonth=randrange(2,13), ayear=randrange(1900,2016))
            for i in range(3)
]

@pytest.mark.parametrize("contact", testdata, ids=[str(x) for x in testdata])
def test_add_contact(app, contact):
    old_contacts = app.contact.get_contact_list()
    app.contact.create(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)