
from model.contact import Contact
from random import randrange

def test_change_in_the_contact(app,db):
    if len(db.get_contact_list()) == 0:
        app.contact.add(Contact(bday="//div[@id='content']/form/select[1]//option[4]",
                                bmonth= "//div[@id='content']/form/select[2]//option[3]",
                                aday="//div[@id='content']/form/select[3]//option[19]",
                                amonth="//div[@id='content']/form/select[4]//option[3]",
                                address2="Test ", privatephone="Test",
                                comments="Test"
                                ))

    old_contacts = db.get_contact_list()
    index = randrange(len(old_contacts))
    contact = Contact(firstname= "New name", lastname = "New name", birthyear="Test", annyear="Test",
                                bday="//div[@id='content']/form/select[1]//option[4]",
                                bmonth= "//div[@id='content']/form/select[2]//option[3]",
                                aday="//div[@id='content']/form/select[3]//option[19]",
                                amonth="//div[@id='content']/form/select[4]//option[3]",
                                )
    contact.id = old_contacts[index].id
    app.contact.change_contact_by_id(index, contact)
    new_contacts = db.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts[index] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
