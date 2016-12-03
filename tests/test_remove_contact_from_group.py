from model.contact import Contact
from model.group import Group
import random


def test_remove_contact_from_group(app, db, orm):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="New one"))
    if len(db.get_contact_list()) == 0:
        app.contact.add(Contact(firstname="Anna", middlename="Joanna", lastname="Wyszomirska", nickname="aneczka",
                                title="Title", company="New Company", address="My address information",
                                home="34725475263", mobile="32456234236", work="2364623645", fax="243256452",
                                email="aniawzs@wp.pl", email2="test1@gmail.com", email3="test2@gmail.com",
                                homepage="Test", birthyear="1990", annyear="2016",
                                bday="//div[@id='content']/form/select[1]//option[4]",
                                bmonth= "//div[@id='content']/form/select[2]//option[3]",
                                aday="//div[@id='content']/form/select[3]//option[19]",
                                amonth="//div[@id='content']/form/select[4]//option[3]",
                                address2="My second address ", privatephone="23415257354735",
                                comments="Brak uwag"
                                ))
    group_id = app.group.random_group_id()
    contacts_in_group = app.contact.get_contacts_in_group(group_id)
    if len(contacts_in_group) == 0:
        ui_list = app.contact.get_contact_list()
        contact = random.choice(ui_list)
        app.contact.add_contact_into_group(contact.id, group_id)

    contact = random.choice(contacts_in_group)
    app.contact.remove_contacts_from_group(contact.id, group_id)
    contact_ui = app.contact.get_contacts_in_group(group_id)
    contact_orm = orm.get_contacts_in_group(Group(id=group_id))
    assert sorted(contact_ui, key=Contact.id_or_max) == sorted(contact_orm, key=Contact.id_or_max)