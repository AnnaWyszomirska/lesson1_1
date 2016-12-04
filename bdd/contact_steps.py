from pytest_bdd import given, when, then
from model.contact import Contact
import random


@given('a contact list')
def contact_list(db):
    return db.get_contact_list()

@given("a contact with <firstname>, <lastname>, <address>, <home> and <mobile>")
def new_contact(firstname, lastname, address, home, mobile):
    return Contact(firstname=firstname, lastname=lastname, address=address, home=home, mobile=mobile)

@when ("I add the contact to the list")
def add_new_contact(app, new_contact):
    app.contact.add(new_contact)

@then("the new contact list is equal to the old contact list with the added contact")
def verify_group_added(db, contact_list, new_contact):
    old_contacts = contact_list
    new_contacts = db.get_contact_list()
    old_contacts.append(new_contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

@given("a non-empty contact list")
def non_empty_contact_list(app, db):
    if len(db.get_contact_list()) == 0:
        app.contact.add(Contact(firstname="Aneczka", lastname="Szmyd"))
    return db.get_contact_list()

@given("a random contact from the list")
def random_contact(non_empty_contact_list):
    return random.choice(non_empty_contact_list)

@when("I delete the contact from the list")
def delete_contact(app, random_contact):
    app.contact.delete_contact_by_id(random_contact.id)

@then("the new contact list is equal to the old contact list without the deleted contact")
def verify_contact_deleted(db,  non_empty_contact_list, random_contact):
    old_contacts = non_empty_contact_list
    new_contacts = db.get_contact_list()
    assert len(old_contacts) - 1 == len(new_contacts)
    old_contacts.remove(random_contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

@given("a random contact from the list to edit")
def random_contact_to_change(non_empty_contact_list):
    return random.randrange(len(non_empty_contact_list))

@when("I change the contact from the list")
def change_contact(app, new_contact, random_contact_to_change):
    app.contact.change_contact_by_index(random_contact_to_change, new_contact)

@then("the new contacts list is equal to the old contacts list")
def verify_changed_contact(db, non_empty_contact_list, random_contact_to_change, new_contact):
    old_contacts = non_empty_contact_list
    new_contacts = db.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts[random_contact_to_change] = new_contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
