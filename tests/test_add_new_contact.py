# -*- coding: utf-8 -*-

from model.contact import Contact




def test_add_contact(app, db, json_contact):
    contact = json_contact
    old_contacts = db.get_contact_list()
    app.contact.add(contact)
    new_contacts = db.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key = Contact.id_or_max) == sorted(new_contacts, key = Contact.id_or_max)


# def test_add_contact_using_orm(app, orm, json_contact):
#     contact = json_contact
#     old_contacts = orm.get_contact_list()
#     app.contact.add(contact)
#     new_contacts =orm.get_contact_list()
#     print (new_contacts)
#     old_contacts.append(contact)
#     assert sorted(old_contacts, key = Contact.id_or_max) == sorted(new_contacts, key = Contact.id_or_max)