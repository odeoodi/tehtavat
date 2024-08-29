#Muokkaa edellistä funktiota siten, että funktio saa parametrinaan nopan tahkojen yhteismäärän.
# Muokatun funktion avulla voit heitellä esimerkiksi 21-tahkoista roolipelinoppaa.
# Edellisestä tehtävästä poiketen nopan heittelyä jatketaan pääohjelmassa
# kunnes saadaan nopan maksimisilmäluku, joka kysytään käyttäjältä ohjelman suorituksen alussa.

import random

def heitto(tahkot):
    luku = random.randint(1,tahkot)
    return luku

maksimi = int(input("Moniko tahkoista noppaa heitetään: "))

noppa = heitto(maksimi)
while noppa != maksimi:
    print(noppa)
    noppa = heitto(maksimi)
print(noppa)

