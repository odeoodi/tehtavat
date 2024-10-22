pelit ={"Monopoli", "Shakki", "Cluedo"}
print(pelit)

pelit.add("Domino")
print(pelit)

pelit.remove("Shakki")
print(pelit)

#tämä ei tee mitään, koska Monopoli on jo osa joukkoa:
pelit.add("Monopoli")
print(pelit)

pelit.add("Jenga")
print(pelit)

for p in pelit:
    print(p)
