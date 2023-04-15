import requests
import json

help(requests)
r = requests.get('https://randomuser.me/api')

print(r.content)
person = r.content

print(r.content)
person = json.loads(r.text)

print(person['results'])

class Person:

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    api_name = person['results'][0]['name']['first']
    api_surname = person['results'][0]['name']['last']



