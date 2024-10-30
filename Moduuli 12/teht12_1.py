"""
Kirjoita ohjelma, joka hakee ja tulostaa satunnaisen Chuck Norris -vitsin käyttäjälle.
Käytä seuravalla sivulla esiteltävää rajapintaa: https://api.chucknorris.io/.
Käyttäjälle on näytettävä pelkkä vitsin teksti.
"""

import requests
import json

request = "https://api.chucknorris.io/jokes/random"
answer = requests.get(request).json()

#print(json.dumps(answer, indent=2))
print(answer["value"])