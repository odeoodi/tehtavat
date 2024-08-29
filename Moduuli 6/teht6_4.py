#Kirjoita funktio, joka saa parametrinaan listan kokonaislukuja.
# Ohjelma palauttaa listassa olevien lukujen summan.
# Kirjoita testausta varten pääohjelma, jossa luot listan, kutsut funktiota ja tulostat sen palauttaman summan.

def lukujensumma(luvut):
    summa = 0
    for l in luvut:
        summa += l
    return summa

luvut = []
luku = 0

#tarkistetaan onko annettu syöte luku vai tyhjä merkkijono:
while True:
    luku = input("Kerro luvut yksitellen ja lopeta painamalla Enter: ")
    if luku == "":
        break
    else:
        luku = int(luku)
        luvut.append(luku)

summa = lukujensumma(luvut)
print(summa)