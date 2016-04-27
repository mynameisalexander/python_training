from random import *


def test_add_contact_to_group(app, db):
    contacts = db.get_contact_list()
    contact = choice(contacts)
    group_number = randrange(len(db.get_group_list()))
    app.contact.add_contact_to_group(contact.id, group_number)
