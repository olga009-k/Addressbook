from json import dumps
from faker import Faker
import collections
import json


import datetime
from typing import Optional, Tuple




def fake_person_generator(length, fake):
    for x in range(length):  # xrange in Python 2.7
        yield {'first_name': fake.last_name(),
               'last_name': fake.first_name(),
               'address': ', '.join([fake.country(),  fake.city(), fake.street_name()]),
               'phone': fake.phone_number(),
               'url': fake.url(),
               }


database = []
filename = './src/initial_data'
length   = 10
fake     = Faker() 
fpg = fake_person_generator(length, fake)
pk = 0
with open('%s.json' % filename, 'w') as output:

    persons = [{
            "model": "phonebook.Person",
            "pk": pk + 1,
            "fields": person,
        }
        for pk, person in enumerate(fpg)
    ]
    json.dump(persons, output,indent=4)



#python manage.py loaddata fixture.json
# <img src="data:image/jpg;base64, ${image}"/></img>