#Kirjoita ohjelma, joka kysyy käyttäjältä nimiä siihen saakka, kunnes käyttäjä syöttää tyhjän merkkijonon.
# Kunkin nimen syöttämisen jälkeen ohjelma tulostaa joko tekstin Uusi nimi tai Aiemmin syötetty nimi sen mukaan,
# syötettiinkö nimi ensimmäistä kertaa. Lopuksi ohjelma luettelee syötetyt nimet yksi kerrallaan allekkain
# mielivaltaisessa järjestyksessä. Käytä joukkotietorakennetta nimien tallentamiseen.

nimet = set()
nimi = input("Anna nimi tai lopeta listaus painamalla Enter: ")

while nimi != "":
    if nimi not in nimet:
        nimet.add(nimi)
        print("Uusi nimi")
        nimi = input("Anna nimi tai lopeta listaus painamalla Enter: ")
    elif nimi in nimet:
        print("Aiemmin syötetty")
        nimi = input("Anna nimi tai lopeta listaus painamalla Enter: ")


print(f"Syötetyt nimet ovat: {nimet}")

