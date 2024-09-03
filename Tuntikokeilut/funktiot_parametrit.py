def tervehdi(kerrat, tervehdys):
    kerrat = int(input("Montako kertaa tervehditään?"))
    for i in range(kerrat):
        print(f"{tervehdys} {i+1}. kerran.")
    return

tervehdi(1, "Moi")
tervehdi(1, "hellou")
