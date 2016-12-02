import re
from random import randrange
from model.contact import Contact

def test_contact_on_the_home_page(app, db):
    old_contacts = app.contact.get_contact_list()
    contact_from_db = db.get_contact_list()

    for i in range(len(contact_from_db)):
        db_contact = contact_from_db[i]
        ui_contact = (sorted(old_contacts, key=Contact.id_or_max))[i]
        assert db_contact == ui_contact

def clear(s):
    return re.sub("[() -]", "", s)

