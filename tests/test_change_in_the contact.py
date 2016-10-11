
from model.contact_change import ContactChange

def test_change_in_the_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.change_contact(ContactChange(firstname1="Changed name", middlename1="Changed", lastname1="Changed",
                                nickname1="Changed",
                                title1="Changed title", company1="Changed", address1="Changed address",
                                home1="111111", mobile1="111111", work1="111111", fax1="111111",
                                email1="changed1", email21="changed2", email31="Changed3",
                                address21="changed", privatephone1="222222",
                                comments1="I want to add comment"
                                ))
    app.session.logout()