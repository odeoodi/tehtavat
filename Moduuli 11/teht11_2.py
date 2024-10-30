"""
Kirjoita aiemmin laatimallesi Auto-luokalle aliluokat Sähköauto ja Polttomoottoriauto.
Sähköautolla on ominaisuutena akkukapasiteetti kilowattitunteina. Polttomoottoriauton ominaisuutena on
bensatankin koko litroina. Kirjoita aliluokille alustajat. Esimerkiksi sähköauton alustaja saa parametreinaan
rekisteritunnuksen, huippunopeuden ja akkukapasiteetin. Se kutsuu yliluokan alustajaa kahden ensin mainitun
asettamiseksi sekä asettaa oman kapasiteettinsa. Kirjoita pääohjelma, jossa luot yhden sähköauton (ABC-15, 180 km/h,
52.5 kWh) ja yhden polttomoottoriauton (ACD-123, 165 km/h, 32.3 l). Aseta kummallekin autolle haluamasi nopeus,
käske autoja ajamaan kolmen tunnin verran ja tulosta autojen matkamittarilukemat.
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


    def kulje(self,tunnit):
        self.kuljettu_matka += tunnit*self.nopeus_nyt

class Electric(Auto):
    def __init__(self,akku,rekkari,huippunopeus):
        self.akku = akku
        super().__init__(rekkari,huippunopeus,nopeus_nyt=0,kuljettu_matka=0)

class Bensa(Auto):
    def __init__(self,tankki,rekkari,huippunopeus):
        self.tankki = tankki
        super().__init__(rekkari, huippunopeus, nopeus_nyt=0, kuljettu_matka=0)



autot = []

autot.append(Electric(52.5,"ABC-15",180))
autot.append(Bensa(32.3,"ACD-14",165))

for a in autot:
    a.kiihdyta(random.randint(30, a.huippunopeus))
for a in autot:
    a.kulje(1)

for a in autot:
    print(f"{a.rekkari}: Kuljettu matka: {a.kuljettu_matka} km.")