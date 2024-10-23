"""
Tehtävä on jatkoa aiemmalle autokilpailutehtävälle. Kirjoita Kilpailu-luokka, jolla on ominaisuuksina kilpailun nimi,
 pituus kilometreinä ja osallistuvien autojen lista. Luokassa on alustaja, joka saa parametreinaan nimen,
 kilometrimäärän ja autolistan ja asettaa ne ominaisuuksille arvoiksi. Luokassa on seuraavat metodit:

tunti_kuluu, joka toteuttaa aiemmassa autokilpailutehtävässä mainitut tunnin välein tehtävät toimenpiteet eli arpoo
kunkin auton nopeuden muutoksen ja kutsuu kullekin autolle kulje-metodia.
tulosta_tilanne, joka tulostaa kaikkien autojen sen hetkiset tiedot selkeäksi taulukoksi muotoiltuna.
kilpailu_ohi, joka palauttaa True, jos jokin autoista on maalissa eli se on ajanut vähintään kilpailun
kokonaiskilometrimäärän. Muussa tapauksessa palautetaan False.
Kirjoita pääohjelma, joka luo 8000 kilometrin kilpailun nimeltä "Suuri romuralli".
Luotavalle kilpailulle annetaan kymmenen auton lista samaan tapaan kuin aiemmassa tehtävässä.
Pääohjelma simuloi kilpailun etenemistä kutsumalla toistorakenteessa tunti_kuluu-metodia, jonka jälkeen aina
tarkistetaan kilpailu_ohi-metodin avulla, onko kilpailu ohi. Ajantasainen tilanne tulostetaan tulosta tilanne-metodin
avulla kymmenen tunnin välein sekä kertaalleen sen jälkeen, kun kilpailu on päättynyt.
"""


import random


class Kilpailu:
    def __init__(self, nimi, pituus_km, osallistujat):
        self.nimi = nimi
        self.pituus_km = pituus_km
        self.osallistujat = osallistujat

    def tunti_kuluu(self):
        for k in range(len(self.osallistujat)):
            autot[k].kiihdyta(random.randint(-10, 15))
        for n in range(len(self.osallistujat)):
            autot[n].kulje(1)

    def tulosta_tilanne(self):
        print("Kilpailun tilanne nyt:")
        for l in range(len(self.osallistujat)):
            print(f"Auto: {autot[l].rekkari}\n *Kuljettu matka: {autot[l].kuljettu_matka}km\n *Nopeus nyt: {autot[l].nopeus_nyt}km/h")

    def kilpailu_ohi(self):
        #palauttaa True, jos jokin autoista on maalissa eli se on ajanut vähintään kilpailun
        # kokonaiskilometrimäärän. Muussa tapauksessa palautetaan False.
        for r in range(len(self.osallistujat)):
            if autot[r].kuljettu_matka >= self.pituus_km:
                return True
            else:
                return False




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



autot = []
for i in range(1,11):
    #luodaan rekisterinumero ja huippunopeudet
    rekisteri = "ABC-"+str(i)
    autot.append(Auto(rekisteri,random.randint(100,200)))

ralli = Kilpailu("Suuri Romuralli",8000,autot)

while not ralli.kilpailu_ohi():
    ralli.tunti_kuluu()
    print("\nTunti kulunut\n")
    ralli.tulosta_tilanne()
    ralli.kilpailu_ohi()
print("\nVOITTAJA LÖYDETTY!\n")
ralli.tulosta_tilanne()

'''
print(f"Autojen ominaisuudet:")
for i in range(0,10):
    print(f"Auto: {autot[i].rekkari}\n Nopeus nyt: {autot[i].nopeus_nyt}\n Kuljettu matka: {autot[i].kuljettu_matka}\n Huippu nopeus: {autot[i].huippunopeus}")
'''
