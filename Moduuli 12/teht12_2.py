'''
Tutustu avoimeen OpenWeather-säärajapintaan: https://openweathermap.org/api. Kirjoita ohjelma,
joka kysyy käyttäjältä paikkakunnan nimen ja tulostaa sitä vastaavan säätilan tekstin sekä lämpötilan Celsius-asteina.
Perehdy rajapinnan dokumentaatioon riittävästi. Palveluun rekisteröityminen on tarpeen, jotta saat rajapintapyynnöissä
tarvittavan API-avaimen (API key). Selvitä myös, miten saat Kelvin-asteet muunnettua Celsius-asteiksi.
'''
from symbol import continue_stmt

import requests
import json

kunta = input("Anna paikkakunta: ")
apikey = 'f8ac0005c4aa7003b8ba79129641b89e'


request = f"https://api.openweathermap.org/data/2.5/forecast?q={kunta}&appid={apikey}"

try:
    response = requests.get(request)
    if response.status_code==200:
        the_response = response.json()
except requests.exceptions.RequestException as e:
    print("Virhe. Hakua ei voida suorittaa")


#print(json.dumps(answer, indent=4))
temperature = []

for arvo in the_response:
    lista = the_response["list"]
    for toinenarvo in lista:
        mainjuttu = toinenarvo["main"]  #Haetaan tällä "main"-sanakirjaa
        temppi = mainjuttu["temp"]
        temperature.append(temppi)

print(f"{temperature[0]-273.15:.2} Celsius")

weather = []


lista = the_response["list"]
for toinenarvo in lista:
    weatherkirja = toinenarvo["weather"]
    tila = weatherkirja[0]["description"]
    weather.append(tila)

print(weather[0])

