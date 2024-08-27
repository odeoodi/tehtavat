#Kirjoita ohjelma, joka kysyy käyttäjältä kokonaisluvun ja ilmoittaa, onko se alkuluku.
# Tässä tehtävässä alkulukuja ovat luvut, jotka ovat jaollisia vain ykkösellä ja itsellään.
#Esimerkiksi luku 13 on alkuluku, koska se voidaan jakaa vain luvuilla 1 ja 13 siten, että jako menee tasan.
#Toisaalta esimerkiksi luku 21 ei ole alkuluku, koska se voidaan jakaa tasan myös luvulla 3 tai luvulla 7.

#määritellään range, jolla kokeillaan jaollisuus 1:stä omaan lukuun yhden numeron välein
#jos jaollisuus == 0, luku on jaollinen kokeillulla luvulla. jos näitä on enemmän kuin kaksi, luku ei ole alkuluku

luku = int(input("Anna kokonaisluku: "))

jaollinen = 0

for n in range(1,(luku+1)):
    jaollisuus = luku % n
    if jaollisuus == 0:
        jaollinen = jaollinen + 1

if jaollinen == 2:
    print("Luku on alkuluku")
else:
    print("Luku ei ole alkuluku")
