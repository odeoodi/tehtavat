#Kirjoita ohjelma, joka kysyy käyttäjältä viiden kaupungin nimet yksi kerrallaan
# (käytä for-toistorakennetta nimien kysymiseen) ja tallentaa ne listarakenteeseen.
# Lopuksi ohjelma tulostaa kaupunkien nimet yksi kerrallaan allekkain samassa järjestyksessä kuin ne syötettiin.
# käytä while-toistorakennetta nimien kysymiseen ja for/in toistorakennetta niiden läpikäymiseen.
kaupungit = []


while len(kaupungit) < 5:
    kaupunki = input("Kerro viisi kaupunkia yksi kerrallaan: ")
    kaupungit.append(kaupunki)

for kaupunki in kaupungit:
    print(kaupunki)