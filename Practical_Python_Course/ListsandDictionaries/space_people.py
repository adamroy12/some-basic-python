#JSON - JavaScript Object Notation. Data arranged in lists and dictionaries.

import requests

response = requests.get('http://api.open-notify.org/astros.json')
json = response.json()

print ('The people currently in space are:')
for astronauts in  json['people']:
    print(astronauts['name'])
