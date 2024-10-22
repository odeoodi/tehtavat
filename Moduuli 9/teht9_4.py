"""
Nyt ohjelmoidaan autokilpailu. Uuden auton kuljettu matka alustetaan automaattisesti nollaksi.
Tee pääohjelman alussa lista, joka koostuu kymmenestä toistorakenteella luodusta auto-oliosta.
Jokaisen auton huippunopeus arvotaan 100 km/h ja 200 km/h väliltä. Rekisteritunnus luodaan seuraavasti "ABC-1",
"ABC-2" jne. Sitten kilpailu alkaa. Kilpailun aikana tehdään tunnin välein seuraavat toimenpiteet:

- Jokaisen auton nopeutta muutetaan siten, että nopeuden muutos arvotaan väliltä -10 ja +15 km/h väliltä.
Tämä tehdään kutsumalla kiihdytä-metodia.

- Kaikkia autoja käsketään liikkumaan yhden tunnin ajan. Tämä tehdään kutsumalla kulje-metodia.

- Kilpailu jatkuu, kunnes jokin autoista on edennyt vähintään 10000 kilometriä.

- Lopuksi tulostetaan kunkin auton kaikki ominaisuudet selkeäksi taulukoksi muotoiltuna.
"""
import random

class Auto:
    def __init__(self, rekkari, huippunopeus, nopeus_nyt=0, kuljettu_matka=0):
        self.rekkari = rekkari
        self.huippunopeus = huippunopeus
        self.nopeus_nyt = nopeus_nyt
        self.kuljettu_matka = kuljettu_matka

    def kiihdyta(self, muutos):
        if self.nopeus_nyt + muutos < 0:
            self.nopeus_nyt = 0
        elif self.nopeus_nyt + muutos > self.huippunopeus:
            self.nopeus_nyt = self.huippunopeus
        else:
            self.nopeus_nyt = self.nopeus_nyt + muutos
        return

    def kulje(self,tunnit):
        self.kuljettu_matka += tunnit*self.nopeus_nyt
        return


autot = []
for i in range(1,11):
    #luodaan rekisterinumero ja huippunopeudet
    rekisteri = "ABC-"+str(i)
    autot.append(Auto(rekisteri,random.randint(100,200)))

"""for n in range(0,10):
    #tulostetaan autoille muodostuneet huippunopeudet ja rekisterinumero
    print(autot[n].huippunopeus,autot[n].rekkari)"""

print("Kisa alkaa!")
while autot[0].kuljettu_matka < 10000 or autot[1].kuljettu_matka < 10000 or autot[2].kuljettu_matka < 10000 or autot[3].kuljettu_matka < 10000 or autot[4].kuljettu_matka < 10000 or autot[5].kuljettu_matka < 10000 or autot[6].kuljettu_matka < 10000 or autot[7].kuljettu_matka < 10000 or autot[8].kuljettu_matka < 10000 or autot[9].kuljettu_matka < 10000:
    for auto in range(0,10):
        autot[auto].kiihdyta(random.randint(-10,15))
    """print("Autojen nopeudet:")
    for auto in range(0,10):
        print(f"Auto: {autot[auto].rekkari}, nopeus: {autot[auto].nopeus_nyt} km/h.")"""
    for auto in range(0,10):
        autot[auto].kulje(1)
    """print("Autojen kuljetut matkat nyt:")
    for auto in range(0,10):
        print(f"Auto: {autot[auto].rekkari}, nopeus: {autot[auto].kuljettu_matka} km.")"""
print("")
print("Voittaja on löytynyt!")
print("")
print(f"Autojen ominaisuudet:")
for i in range(0,10):
    print(f"Auto: {autot[i].rekkari}\n Nopeus nyt: {autot[i].nopeus_nyt}\n Kuljettu matka: {autot[i].kuljettu_matka}\n Huippu nopeus: {autot[i].huippunopeus}")

