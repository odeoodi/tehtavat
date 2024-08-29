def tervehdi(tervehdys, kerrat):
    kerrat = int(input("Montako kertaa tervehditään?"))
    for i in range(kerrat):
        print(f"{tervehdys} {i+1}. kerran.")
    return

tervehdi("Moro", 1)
tervehdi("helou", 1)
