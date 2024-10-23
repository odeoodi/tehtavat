"""
Jatka edellisen tehtävän ohjelmaa siten, että teet Talo-luokan. Talon alustajaparametreina annetaan alimman
ja ylimmän kerroksen numero sekä hissien lukumäärä. Talon luonnin yhteydessä talo luo tarvittavan määrän hissejä.
Hissien lista tallennetaan talon ominaisuutena. Kirjoita taloon metodi aja_hissiä, joka saa parametreinaan hissin
numeron ja kohdekerroksen. Kirjoita pääohjelmaan lauseet talon luomiseksi ja talon hisseillä ajelemiseksi.
"""


class Hissi:
    def __init__(self,numero, alin, ylin):
        self.numero = numero
        self.alin = alin
        self.ylin = ylin
        self.kerros_nyt = alin
        self.haluttu_kerros = None


    def kerros_ylos(self,hissi,kerros_nyt):
        self.kerros_nyt = kerros_nyt
        hissi.kerros_nyt += 1
        print(f"Siirrytään ylöspäin hissillä {hissi.numero}. Olet nyt kerroksessa {hissi.kerros_nyt}.")


    def kerros_alas(self,hissi, kerros_nyt):
        self.kerros_nyt = kerros_nyt
        hissi.kerros_nyt -= 1
        print(f"Siirrytään alaspäin hissillä {hissi.numero}. Olet nyt kerroksessa {hissi.kerros_nyt}.")

    def siirry_kerrokseen(self,hissi,haluttu_kerros):
        self.haluttu_kerros = haluttu_kerros
        while self.haluttu_kerros != hissi.kerros_nyt:
            if self.haluttu_kerros < hissi.kerros_nyt:
                hissi.kerros_alas(hissi,hissi.kerros_nyt)
            elif self.haluttu_kerros > hissi.kerros_nyt:
                hissi.kerros_ylos(hissi,hissi.kerros_nyt)
        print(f"Olet nyt haluamassasi kerroksessa: {hissi.kerros_nyt}")

class Talo:
    def __init__(self,alin,ylin,hissien_lkm):
        self.alin = alin
        self.ylin = ylin
        self.hissien_lkm = hissien_lkm
        self.hissit = []
        for i in range(hissien_lkm):
            self.hissit.append(Hissi(i+1,alin,ylin))

    def aja_hissia(self,hissinro,kohde):
        self.hissit[hissinro-1].siirry_kerrokseen(self.hissit[hissinro-1],kohde)


talo1 = Talo(0, 10, 5)

for hissi in range(5):
    print(talo1.hissit[hissi].numero)
talo1.aja_hissia(2,5)
talo1.aja_hissia(3,9)
talo1.aja_hissia(3,5)
talo1.aja_hissia(2,3)
'''
hissi_a = Hissi(0,50)
hissi_a.siirry_kerrokseen(hissi_a,25)
hissi_a.siirry_kerrokseen(hissi_a,15)
'''