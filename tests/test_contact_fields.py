import re
from random import randrange
from model.contact import Contact

def test_contact_on_the_home_page(app, db):
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    contact_from_home_page = sorted(app.contact.get_contact_list(), key=Contact.id_or_max)[index]
    #contact_from_edit_page = app.contact.get_contact_info_from_edit_page#(index)
    contact_from_db = db.get_contact_list()[index]


    # for i in range(len(contact_from_home_page)):
    #     print(sorted(contact_from_home_page, key=Contact.id_or_max)[i])
    #     print(sorted(contact_from_db, key=Contact.id_or_max)[i])
    #     assert sorted(contact_from_home_page, key=Contact.id_or_max)[i] == sorted(contact_from_db, key=Contact.id_or_max)[i]
    # assert [x for x in (sorted(contact_from_home_page, key=Contact.id_or_max), sorted(contact_from_db, key=Contact.id_or_max))]

    for i in range(index):
        assert contact_from_home_page.firstname == contact_from_db.firstname
        assert contact_from_home_page.lastname == contact_from_db.lastname
        assert contact_from_home_page.address == contact_from_db.address
        assert contact_from_home_page.all_emails_form_home_page == merge_emails_like_on_homepage(contact_from_db)
        assert contact_from_home_page.all_phones_from_home_page == merge_phones_like_on_homepage(contact_from_db)


def clear(s):
    return re.sub("[() -]", "", s)

# def merge_emails_like_on_homepage(contact):
#     return "\n".join(filter(lambda x: x != "",(filter(lambda x: x is not None,[contact.email, contact.email2, contact.email3]))))
#
# def merge_phones_like_on_homepage(contact):
#     return "\n".join(filter(lambda x: x != "",
#                                 map(lambda x: clear(x),
#                                     filter(lambda x: x is not None,
#                                            [contact.home, contact.mobile, contact.work, contact.privatephone]))))


def merge_emails_like_on_homepage(db):
    return "\n".join(filter(lambda x: x != "",(filter(lambda x: x is not None,[db.email, db.email2, db.email3]))))

def merge_phones_like_on_homepage(db):
    return "\n".join(filter(lambda x: x != "",
                                map(lambda x: clear(x),
                                    filter(lambda x: x is not None,
                                           [db.home, db.mobile, db.work,db.privatephone]))))