from model.contact import Contact
import random
import string
import os.path
import jsonpickle
import getopt
import sys

try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of contacts", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

n = 5
f = "data/contact.json"

for o,a in opts:
    if o =="-n":
        n=int(a)
    elif o =="-f":
        f =a

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


file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

with open(file, "w") as out:
    jsonpickle.set_encoder_options('json', indent = 2)
    out.write(jsonpickle.encode(testdata))