from random import *
from fixture import contact


def test_remove_contact_from_group(app, db):
    contacts = db.get_contact_list()
    contact = choice(contacts)
    group_number = randrange(len(db.get_group_list()))
    while contact.check_add_contact() == None:
        app.test_add_contact_to_group(app, db)
    app.contact.remove_contact_from_group(contact.id, group_number+3)

