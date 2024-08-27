#Kirjoita ohjelma, joka kysyy käyttäjältä arpakuutioiden lukumäärän.
# Ohjelma heittää kerran kaikkia arpakuutioita ja tulostaa silmälukujen summan. Käytä for-toistorakennetta.
import random

noppa = int(input("Anna arpakuutioiden lukumäärä: "))
summa = 0

print("")
for n in range(1,noppa):
    luku = random.randint(1,6)
    summa = summa+luku

print(f"Summa on {summa}")
