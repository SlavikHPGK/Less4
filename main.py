import requests
import json
from colorama import Fore, Back, Style

help(requests)
r = requests.get('https://randomuser.me/api')

print(r.content)
person = r.content

print(r.content)
person = json.loads(r.text)

print(person['results'])

class Person:

    def __init__(self, name, surname, age ,gender):
        self.name = name
        self.surname = surname
        self.age = age
        self.gender = gender

api_name = person['results'][0]['name']['first']
api_surname = person['results'][0]['name']['last']
api_age = person['results'][0]['dob']['age']
api_gender = person['results'][0]['gender']

user = Person(api_name, api_surname, api_age, api_gender)

try:
    print(Fore.BLUE + user)
else:

try:
    print(23/0)
except:
    print('error')