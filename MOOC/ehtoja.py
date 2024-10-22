'''
Tee ohjelma, joka kysyy käyttäjältä kolme kirjainta. Ohjelma tulostaa kirjaimista aakkosjärjestyksessä keskimmäisen.

Voit olettaa, että kirjaimet ovat joko kaikki isoja tai kaikki pieniä kirjaimia.
'''

eka = input("Anna 1. kirjain: ")
toka = input("Anna 2. kirjain: ")
kolmas = input("Anna 3. kirjain: ")

if eka > toka > kolmas or kolmas > toka > eka:
    print(f"Keskimmäinen kirjain on {toka}")
elif toka > eka > kolmas or kolmas > eka > toka:
    print(f"Keskimmäinen kirjain on {eka}")
else:
    print(f"Keskimmäinen kirjain on {kolmas}")