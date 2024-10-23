"""
Kirjoita Hissi-luokka, joka saa alustajaparametreinaan alimman ja ylimmän kerroksen numeron. Hissillä on metodit
 siirry_kerrokseen, kerros_ylös ja kerros_alas. Uusi hissi on aina alimmassa kerroksessa.
Jos tee luodulle hissille h esimerkiksi metodikutsun h.siirry_kerrokseen(5), metodi kutsuu joko kerros_ylös-
tai kerros_alas-metodia niin monta kertaa, että hissi päätyy viidenteen kerrokseen. Viimeksi mainitut metodit
ajavat hissiä yhden kerroksen ylös- tai alaspäin ja ilmoittavat, missä kerroksessa hissi sen jälkeen on.
Testaa luokkaa siten, että teet pääohjelmassa hissin ja käsket sen siirtymään haluamaasi kerrokseen ja
sen jälkeen takaisin alimpaan kerrokseen.
"""

class Hissi:
    def __init__(self, alin, ylin):
        self.alin = alin
        self.ylin = ylin
        self.kerros_nyt = alin
        self.haluttu_kerros = None


    def kerros_ylos(self,hissi,kerros_nyt):
        self.kerros_nyt = kerros_nyt
        hissi.kerros_nyt += 1
        print(f"Siirrytään ylöspäin. Olet nyt kerroksessa {hissi.kerros_nyt}.")


    def kerros_alas(self,hissi, kerros_nyt):
        self.kerros_nyt = kerros_nyt
        hissi.kerros_nyt -= 1
        print(f"Siirrytään alaspäin. Olet nyt kerroksessa {hissi.kerros_nyt}.")

    def siirry_kerrokseen(self,hissi,haluttu_kerros):
        self.haluttu_kerros = haluttu_kerros
        while self.haluttu_kerros != hissi.kerros_nyt:
            if self.haluttu_kerros < hissi.kerros_nyt:
                hissi.kerros_alas(hissi,hissi.kerros_nyt)
            elif self.haluttu_kerros > hissi.kerros_nyt:
                hissi.kerros_ylos(hissi,hissi.kerros_nyt)
        print(f"Olet nyt haluamassasi kerroksessa: {hissi.kerros_nyt}")



hissi_a = Hissi(0,50)
hissi_a.siirry_kerrokseen(hissi_a,25)
hissi_a.siirry_kerrokseen(hissi_a,15)