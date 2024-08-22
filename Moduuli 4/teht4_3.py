luku = input("Anna luku: ")

if luku.isdigit():
    luku = int(luku)
    suurin = luku
    pienin = luku
else:
    print(f"Suurin luku on {suurin} ja pienin luku on {pienin}")

while True:
    syote = input("Anna luku: ")
    if syote == "":
        break

    if syote.isdigit():
        luku = int(syote)
    if luku > suurin:
        suurin = luku
    if luku < pienin:
        pienin = luku

print(f"Suurin luku on {suurin} ja pienin luku on {pienin}")

