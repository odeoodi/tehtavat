'''
Tutustu avoimeen OpenWeather-säärajapintaan: https://openweathermap.org/api. Kirjoita ohjelma,
joka kysyy käyttäjältä paikkakunnan nimen ja tulostaa sitä vastaavan säätilan tekstin sekä lämpötilan Celsius-asteina.
Perehdy rajapinnan dokumentaatioon riittävästi. Palveluun rekisteröityminen on tarpeen, jotta saat rajapintapyynnöissä
tarvittavan API-avaimen (API key). Selvitä myös, miten saat Kelvin-asteet muunnettua Celsius-asteiksi.
'''

import requests
import json

kunta = input("Anna paikkakunta: ")
apikey = 'f8ac0005c4aa7003b8ba79129641b89e'


request = f"https://api.openweathermap.org/data/2.5/forecast?q={kunta}&appid={apikey}"
answer = requests.get(request).json()

#print(json.dumps(answer, indent=4))
temperature = []

for arvo in answer:
    lista = answer["list"]
    for toinenarvo in lista:
        mainjuttu = toinenarvo["main"]  #Haetaan tällä "main"-sanakirjaa
        temppi = mainjuttu["temp"]
        temperature.append(temppi)

print(f"{temperature[0]-273.15:.2} Celsius")

weather = []


lista = answer["list"]
for toinenarvo in lista:
    weatherkirja = toinenarvo["weather"]
    tila = weatherkirja[0]["description"]
    weather.append(tila)

print(weather[0])

