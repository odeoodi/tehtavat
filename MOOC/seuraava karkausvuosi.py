'''
Tee ohjelma, joka kyselee käyttäjältä vuosilukua ja kertoo, milloin on seuraava karkausvuosi.
Jos käyttäjän syöttämä vuosi on karkausvuosi (kuten 2020),
ohjelma ei kerro tätä vuotta vaan sitä seuraavan karkausvuoden:
'''

vuosi = int(input("Vuosi: "))
def karkausvuosi(annettu_vuosi):
    #onko karkausvuosi:
    if (annettu_vuosi % 4 == 0 and annettu_vuosi % 100 != 0) or annettu_vuosi%400==0:
        karkuri = annettu_vuosi
    else:
        karkuri = annettu_vuosi+1
    return karkuri

oikea_karkuri = karkausvuosi(vuosi)
print(oikea_karkuri)

if vuosi == oikea_karkuri:
    print(f"Vuotta {vuosi} seuraava karkausvuosi on {vuosi+4}")
else:
    while not (oikea_karkuri % 4 == 0 and oikea_karkuri % 100 != 0) or oikea_karkuri % 400 == 0:
        oikea_karkuri+=1
        print(oikea_karkuri)
    print(f"Vuotta {vuosi} seuraava karkausvuosi on {oikea_karkuri}")