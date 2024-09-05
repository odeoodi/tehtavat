#Kirjoita funktio, joka saa parametreinaan pyöreän pizzan halkaisijan senttimetreinä sekä pizzan hinnan euroina.
# Funktio laskee ja palauttaa pizzan yksikköhinnan euroina per neliömetri. Pääohjelma kysyy käyttäjältä kahden
# pizzan halkaisijat ja hinnat sekä ilmoittaa, kumpi pizza antaa paremman vastineen rahalle (eli kummalla on
# alhaisempi yksikköhinta). Yksikköhintojen laskennassa on hyödynnettävä kirjoitettua funktiota.
import math


def epernelio(halkaisija, hinta):
    neliohinta = hinta/((((halkaisija)/100/2)**2)*math.pi)
    return neliohinta

senttim = float(input("Kerro 1. pizzan halkaisija (cm): "))
eurot = float(input("Kerro 1. pizzan hinta: "))

eka = epernelio(senttim, eurot)
print(f"Ekan pizzan neliöhinta: {eka:2.2f} €/m2")

senttim2 = float(input("Kerro 2. pizzan halkaisija (cm): "))
eurot2 = float(input("Kerro 2. pizzan hinta: "))

toka = epernelio(senttim2, eurot2)
print(f"Ekan pizzan neliöhinta: {toka:2.2f} €/m2")

if eka < toka:
    print("Ensimmäinen pitsa antaa paremmin vastinetta rahalle.")
elif toka < eka:
    print("Toinen pitsa antaa paremmin vastinetta rahalle.")
else:
    print("Pitsat ovat identtiset!")
