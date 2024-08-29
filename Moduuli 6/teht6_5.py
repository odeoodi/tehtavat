#Kirjoita funktio, joka saa parametrinaan listan kokonaislukuja. Ohjelma palauttaa toisen listan,
# joka on muuten samanlainen kuin parametrina saatu lista paitsi että siitä on karsittu pois kaikki
# parittomat luvut. Kirjoita testausta varten pääohjelma, jossa luot listan, kutsut funktiota ja tulostat sen
# jälkeen sekä alkuperäisen että karsitun listan.

def parilliset(lukuja):
    pari = []
    for l in lukuja:
        if l % 2 == 0:
            pari.append(l)
    return pari

kokonaislukuja = [1,2,3,4,5,6,7,8,9,10]
uusilista = parilliset(kokonaislukuja)

print(uusilista)