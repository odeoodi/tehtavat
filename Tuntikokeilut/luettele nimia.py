nimet = []

nimi = input("Anna nimi tai lopeta painamalla Enter: ")
while nimi!="":
    nimet.append(nimi)
    nimi = input("Anna nimi tai lopeta painamalla Enter: ")

nimet.sort()
print(nimet)

for n in nimet:
    print (f"Moi, {n}!")
# eli suorittaa alla olevan toiminnon niin monta kertaa, kuin listassa on alkioita. Sijoittaa {n} kohdalle sen hetkisen
# alkion listasta.



