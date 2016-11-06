# -*- coding: utf-8 -*-

from model.contact import Contact
import pytest
import random
import string

def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation+ " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

def random_day():
    day = [x for x in range(1,32)]
    return random.choice(day)

def random_month():
    month = ["Styczeń", "Luty", "Marzec", "Kwiecień", "Maj", "Czerwiec", "Lipiec", "Sierpień", "Wrzesień", "Październik", "Listopad", "Grudzień"]
    return random.choice(month)

testdata = [
        Contact(firstname=firstname, middlename=middlename, lastname=lastname, nickname=nickname,
                            title=title, company=company, address=address, home=home, mobile=mobile, work=work, fax=fax,
                            email=email, email2=email2, email3=email3, homepage=homepage, birthyear=birthyear, annyear=annyear,
                            bday= bday, bmonth= bmonth, aday=aday, amonth=amonth, address2= address2, privatephone=privatephone,  comments=comments)
        for firstname in ["", random_string("firstname", 5)]
        for middlename in ["", random_string("middlename", 10)]
        for lastname in ["", random_string("lastname", 10)]
        for nickname in ["", random_string("nickname", 10)]
        for title in ["", random_string("title", 7)]
        for company in ["", random_string("company", 20)]
        for address in ["", random_string("header", 30)]
        for home in ["", random_string("home", 10)]
        for mobile in ["", random_string("mobile", 10)]
        for work in ["", random_string("work", 10)]
        for fax in ["", random_string("fax", 10)]
        for email in ["", random_string("email", 15)]
        for email2 in ["", random_string("email2", 15)]
        for email3 in ["", random_string("email3", 15)]
        for homepage in ["", random_string("homepage", 20)]
        for birthyear in ["", random_string("birthyear", 20)]
        for annyear in ["", random_string("annyear", 20)]
        for bday in ["", random_day]
        for bmonth in ["", random_month]
        for aday in ["", random_day]
        for amonth in ["", random_month]
        for address2 in ["", random_string("address2", 20)]
        for privatephone in ["", random_string("privatephone", 20)]
        for comments in ["", random_string("comments", 20)]
        ]

@pytest.mark.parametrize("contact", testdata, ids=[repr(x) for x in testdata])
def test_add_contact(app, contact):
    old_contacts = app.contact.get_contact_list()
    app.contact.add(contact)
    assert len(old_contacts) + 1 == app.contact.count_contact()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key = Contact.id_or_max) == sorted(new_contacts, key = Contact.id_or_max)