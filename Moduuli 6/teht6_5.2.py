import random

def parilliset(lukuja):
    pari = []
    for l in lukuja:
        if l % 2 == 0:
            pari.append(l)
            pari.sort()
    return pari

kokonaislukuja = []

while len(kokonaislukuja) < 20:
    numero = random.randint(1,100)
    if numero not in kokonaislukuja:
        kokonaislukuja.append(numero)

uusilista = parilliset(kokonaislukuja)

print(uusilista)