from model.contact import Contact
from random import *
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

n = 3
f = "data/contacts.json"

for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + " "*10
    return prefix + "".join([choice(symbols) for i in range(randrange(maxlen))])


testdata = [
    Contact(firstname="",   middlename="",  lastname="",    nickname="",
            title="",       company="",     address="",     homephone="",
            mobilephone="", workphone="",   fax="",         email="",
            email2="",      email3="",      homepage="",    bday=None,
            bmonth=None,    byear=None,     aday=None,      amonth=None,
            ayear=None,     address2="",    secondphone="", notes="")] + [
    Contact(firstname=random_string("firstname", 10),     middlename=random_string("middlenam", 10),
            lastname=random_string("lastname", 10),       nickname=random_string("nickname", 10),
            title=random_string("title", 10),             company=random_string("company", 10),
            address=random_string("address", 20),         homephone=random_string("homephone", 10),
            mobilephone=random_string("mobilephone", 10), workphone=random_string("workphone", 10),
            fax=random_string("fax", 10),                 email=random_string("workphone", 10),
            email2=random_string("email2", 10),           email3=random_string("email3", 10),
            homepage=random_string("homepage", 10),       address2=random_string("address2", 20),
            secondphone=random_string("secondphone", 20), notes=random_string("notes", 20),
            bday=randrange(3,33), bmonth=randrange(2,13), byear=randrange(1900,2016),
            aday=randrange(3,33), amonth=randrange(2,13), ayear=randrange(1900,2016))
            for i in range(n)
]


file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../", f)


with open(file, "w") as out:
    jsonpickle.set_encoder_options("json", indent=2)
    out.write(jsonpickle.encode(testdata))