tunnus = input("Anna käyttäjätunnus: ")
salasana = input("Anna salasana: ")

yritykset = 0

if tunnus == "python" and salasana == "rules":
    print("Tervetuloa!")

while tunnus != "python" or salasana != "rules":
    yritykset += 1
    print(f"Yritä uudelleen, sinulla on vielä {5 - yritykset} yritystä.")
    tunnus = input("Anna käyttäjätunnus uudelleen: ")
    salasana = input("Anna salasana uudelleen: ")
    if yritykset > 5:
        print("Pääsy evätty.")
        break