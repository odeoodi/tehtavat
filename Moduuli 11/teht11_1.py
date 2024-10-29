"""
Toteuta seuraava luokkahierarkia Python-kielellä: Julkaisu voi olla kirja tai lehti. Jokaisella julkaisulla on nimi.
Kirjalla on lisäksi kirjoittaja ja sivumäärä, kun taas lehdellä on päätoimittaja. Kirjoita luokkiin myös tarvittavat
alustajat. Tee aliluokkiin metodi tulosta_tiedot, joka tulostaa kyseisen julkaisun kaikki tiedot. Luo pääohjelmassa
julkaisut Aku Ankka (päätoimittaja Aki Hyyppä) ja Hytti n:o 6 (kirjailija Rosa Liksom, 200 sivua).
Tulosta molempien julkaisujen kaikki tiedot toteuttamiesi metodien avulla.
"""

class Julkaisu:
    def __init__(self,nimi):
        self.nimi = nimi

class Lehti(Julkaisu):
    def __init__(self,toimittaja,nimi):
        self.toimittaja = toimittaja
        super().__init__(nimi)

    def tulosta_tiedot(self):
        print(f"Julkaisun nimi on {self.nimi} ja päätoimittaja {self.toimittaja}.")

class Kirja(Julkaisu):
    def __init__(self,nimi,sivunro,kirjailija):
        self.sivunro = sivunro
        self.kirjailija = kirjailija
        super().__init__(nimi)

    def tulosta_tiedot(self):
        print(f"Julkaisun nimi on {self.nimi}, kirjailija on {self.kirjailija} ja sivumäärä {self.sivunro} sivua.")

julkaisut = []
julkaisut.append(Lehti("Aki Hyyppä", "Aku Ankka"))
julkaisut.append(Kirja("Hytti n:o 6",200,"Rosa Liksom"))

for k in julkaisut:
    k.tulosta_tiedot()


