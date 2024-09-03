#Kirjoita ohjelma, joka kysyy käyttäjältä kuukauden numeron, jonka jälkeen ohjelma tulostaa sitä
# vastaavan vuodenajan (kevät, kesä, syksy, talvi). Tallenna ohjelmassasi kuukausia vastaavat vuodenajat
# merkkijonoina monikkotietorakenteeseen. Määritellään kukin vuodenaika kolmen kuukauden mittaiseksi siten,
# että joulukuu on ensimmäinen talvikuukausi.

vuodenajat = ("talvi", "kevät", "kesä", "syksy")

kuukausi = int(input("Kerro kuukauden numero: "))

if kuukausi==12 or 1<kuukausi<3:
    aika = 0
elif 2<kuukausi <=5:
    aika = 1
elif 5<kuukausi<=8:
    aika = 2
elif 8<kuukausi<12:
    aika = 3
else:
    print("Tämä ei ole mikään kuukausi...")


if 1<=kuukausi<=12:
    vuodenaika = vuodenajat[aika]
    print(f"Vuodenaika on silloin {vuodenaika}.")


