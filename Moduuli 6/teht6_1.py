#Kirjoita parametriton funktio, joka palauttaa paluuarvonaan satunnaisen nopan silmäluvun väliltä 1..6.
# Kirjoita pääohjelma, joka heittää noppaa niin kauan kunnes tulee kuutonen.
# Pääohjelma tulostaa kunkin heiton jälkeen saadun silmäluvun.
import random

def heitto():
    luku = random.randint(1,6)
    return luku


noppa = heitto()
while noppa != 6:
    print(noppa)
    noppa = heitto()
print(noppa)


