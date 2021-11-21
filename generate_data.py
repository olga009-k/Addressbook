from json import dumps
from faker import Faker
import collections
import json


import datetime
from typing import Optional, Tuple

import requests
import numpy as np
import base64
from PIL import Image



def get_random_photo() -> Optional[np.ndarray]:
    for _ in range(1):  # repeats to download image
        try:
            r = requests.get('https://100k-faces.glitch.me/random-image-url')
            url = r.json()['url']
            print(url)
            im = Image.open(requests.get(url, stream=True).raw)
            im = im.resize((50, 50))
            im = np.array(im) 
            base64_bytes = base64.b64encode(im)
            base64_string = base64_bytes.decode('utf-8')
            return "data:image/jpg;base64," + base64_string
        except Exception:
            continue
    return None


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