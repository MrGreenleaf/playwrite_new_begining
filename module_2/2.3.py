import json

with open('contacts.json', 'r') as file:
    user = json.loads(file)