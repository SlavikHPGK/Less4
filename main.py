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


