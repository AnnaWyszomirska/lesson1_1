
from model.contact import Contact

def test_change_in_the_contact(app):
    if app.contact.count_contact == 0:
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


    app.contact.change_contact(Contact(firstname="Changed name", middlename="Changed", lastname="Changed",
                                nickname="Changed",
                                title="Changed title", company="Changed", address="Changed address",
                                home="111111", mobile="111111", work="111111", fax="111111",
                                email="changed1", email2="changed2", email3="Changed3",
                                homepage="Changed", birthyear="1995", annyear="2012",
                                bday="//div[@id='content']/form/select[1]//option[4]",
                                bmonth="//div[@id='content']/form/select[2]//option[3]",
                                aday="//div[@id='content']/form/select[3]//option[19]",
                                amonth="//div[@id='content']/form/select[4]//option[3]",
                                address2="changed", privatephone="222222",
                                comments="I want to add comment"
                                ))
