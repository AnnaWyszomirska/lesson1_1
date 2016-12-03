import re
from random import randrange
from model.contact import Contact

def test_contact_on_the_home_page(app, db):
    old_contacts = app.contact.get_contact_list()
    contact_from_db = db.get_contact_list()

    for i in range(len(contact_from_db)):
        db_contact = contact_from_db[i]
        ui_contact = (sorted(old_contacts, key=Contact.id_or_max))[i]
        assert ui_contact.firstname == db_contact.firstname
        assert ui_contact.lastname == db_contact.lastname
        assert ui_contact.address == db_contact.address
        assert ui_contact.all_emails_form_home_page == merge_emails_like_on_homepage(db_contact)
        assert ui_contact.all_phones_from_home_page == merge_phones_like_on_homepage(db_contact)


def clear(s):
    return re.sub("[() -]", "", s)


def merge_emails_like_on_homepage(db):
    return "\n".join(filter(lambda x: x != "",(filter(lambda x: x is not None,[db.email, db.email2, db.email3]))))

def merge_phones_like_on_homepage(db):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,[db.home, db.mobile, db.work,db.privatephone]))))
