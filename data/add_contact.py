from model.contact import Contact
import random
import string

constant = [
    Contact (firstname="Joanna", lastname="Testowa", bday="1",bmonth="Styczeń"),
    Contact(firstname="Basia", lastname="Kowalska", bday="2", bmonth="Luty"),
]

def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation+ " "*2
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

def random_day():
    day = [x for x in range(1,32)]
    return random.choice(day)

def random_month():
    month = ["Styczeń", "Luty", "Marzec", "Kwiecień", "Maj", "Czerwiec", "Lipiec", "Sierpień", "Wrzesień", "Październik", "Listopad", "Grudzień"]
    return random.choice(month)

testdata = [Contact(firstname="", lastname="", bday= "",bmonth="")] + [
        Contact(firstname=random_string("firstname", 20), lastname=random_string("lastname", 20),
                bday= random_day(),bmonth= random_month())
        for i in range(3)
        ]

