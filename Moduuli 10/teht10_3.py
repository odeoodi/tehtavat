"""
Jatka edellisen tehtävän ohjelmaa siten, että Talo-luokassa on parametriton metodi palohälytys,
joka käskee kaikki hissit pohjakerrokseen. Jatka pääohjelmaa siten, että talossasi tulee palohälytys.
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

    def tulipalo(self):
        print(f"Rakennuksessa on tulipalo, hissit laskeutuvat automaattisesti kerrokseen {self.alin}.\n")
        for hissi in range(int(self.hissien_lkm)):
            self.hissit[hissi].siirry_kerrokseen(self.hissit[hissi],0)

talo1 = Talo(0, 10, 5)
talo2 = Talo(1,50,6)
for hissi in range(5):
    print(talo1.hissit[hissi].numero)
talo1.aja_hissia(2,5)
talo1.aja_hissia(3,9)
talo1.aja_hissia(3,5)
talo1.aja_hissia(2,3)
talo1.aja_hissia(5,8)
talo1.aja_hissia(1,2)
talo1.aja_hissia(4,6)
talo1.tulipalo()
