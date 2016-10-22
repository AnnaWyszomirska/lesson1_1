
from model.contact import Contact

def test_change_in_the_contact(app):
    if app.contact.count_contact() == 0:
        app.contact.add(Contact(firstname="Test", middlename="Test", lastname="Test", nickname="Test",
                                title="Test", company="Test", address="Test",
                                home="Test", mobile="Test", work="Test", fax="Test",
                                email="Test", email2="Test", email3="Test",
                                homepage="Test", birthyear="Test", annyear="Test",
                                bday="//div[@id='content']/form/select[1]//option[4]",
                                bmonth= "//div[@id='content']/form/select[2]//option[3]",
                                aday="//div[@id='content']/form/select[3]//option[19]",
                                amonth="//div[@id='content']/form/select[4]//option[3]",
                                address2="Test ", privatephone="Test",
                                comments="Test"
                                ))

    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname="Test", middlename="Test", lastname="Test", nickname="Test",
                                title="Test", company="Test", address="Test",
                                home="Test", mobile="Test", work="Test", fax="Test",
                                email="Test", email2="Test", email3="Test",
                                homepage="Test", birthyear="Test", annyear="Test",
                                bday="//div[@id='content']/form/select[1]//option[4]",
                                bmonth= "//div[@id='content']/form/select[2]//option[3]",
                                aday="//div[@id='content']/form/select[3]//option[19]",
                                amonth="//div[@id='content']/form/select[4]//option[3]",
                                address2="Test ", privatephone="Test",
                                comments="Test")
    contact.id = old_contacts[0].id
    app.contact.change_contact(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts[0] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
