import random

pisteet = int(input("Pisteiden kokonaismäärä: "))

ympyra = 0
kokeiltu = 0

while kokeiltu <= pisteet:
    x_koord = random.uniform(-1,1)
    y_koord = random.uniform(-1,1)
    if x_koord**2 + y_koord**2 < 1:
        ympyra +=1
    kokeiltu +=1

print((ympyra*4)/kokeiltu)