import random

luku = random.randint(1,10)

arvaus = int(input("Arvaa luku: "))


while arvaus != luku:
    if arvaus > luku:
        print("Liian suuri arvaus.")
    elif arvaus < luku:
        print("Liian pieni arvaus.")
    arvaus = int(input("Arvaa luku: "))
print("Oikein!")