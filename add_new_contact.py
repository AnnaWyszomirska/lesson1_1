# -*- coding: utf-8 -*-

import pytest
from contact import Contact
from contactapplication import ContactApplication

@pytest.fixture
def contapp(request):
    fixture = ContactApplication()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_add_contact(contapp):
    contapp.login(username="admin", password="secret")
    contapp.add_contact_detail(Contact(firstname="Anna", middlename="Joanna", lastname="Wyszomirska", nickname="aneczka",
                                            title="Title", company="New Company",address="My address information",
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

    contapp.logout()

