"""
Laajenna ohjelmaa siten, että mukana on kulje-metodi, joka saa parametrinaan tuntimäärän.
Metodi kasvattaa kuljettua matkaa sen verran kuin auto on tasaisella vauhdilla annetussa tuntimäärässä edennyt.
Esimerkki: auto-olion tämänhetkinen kuljettu matka on 2000 km. Nopeus on 60 km/h.
Metodikutsu auto.kulje(1.5) kasvattaa kuljetun matkan lukemaan 2090 km.
"""


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
        self.kuljettu_matka = tunnit*self.nopeus_nyt
        return




auto1 = Auto("ABC-123", 142)

auto1.kiihdyta(70)
auto1.kiihdyta(50)
print(f"Auton nopeus tällä hetkellä on: {auto1.nopeus_nyt:d} km/h.")
auto1.kulje(2)
print(f"Auto on kulkenut tähän mennessä {auto1.kuljettu_matka} kilometriä.")
