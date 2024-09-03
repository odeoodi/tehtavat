#Kirjoita ohjelma lentoasematietojen hakemiseksi ja tallentamiseksi. Ohjelma kysyy käyttäjältä, haluaako
# tämä syöttää uuden lentoaseman, hakea jo syötetyn lentoaseman tiedot vai lopettaa. Jos käyttäjä valitsee
# uuden lentoaseman syöttämisen, ohjelma kysyy käyttäjältä lentoaseman ICAO-koodin ja nimen. Jos käyttäjä valitsee
# haun, ohjelma kysyy ICAO-koodin ja tulostaa sitä vastaavan lentoaseman nimen. Jos käyttäjä haluaa lopettaa,
# ohjelman suoritus päättyy. Käyttäjä saa valita uuden toiminnon miten monta kertaa tahansa aina siihen asti,
# kunnes hän haluaa lopettaa. (ICAO-koodi on lentoaseman yksilöivä tunniste. Esimerkiksi Helsinki-Vantaan
# lentoaseman ICAO-koodi on EFHK. Löydät koodeja helposti selaimen avulla.)

print("Mitä haluat tehdä? \n- Syöttää uuden lentoaseman tiedot \n- Hakea jo syötetyn lentoaseman tietoja \n- Lopettaa")
toiminto = input("Kirjoita toiminto: 'uusi tieto', 'haku' tai 'lopeta': ")

kentat = {}
kentat["EFHK"]="Helsinki-Vantaa"

while toiminto != "lopeta":
    if toiminto == "uusi tieto":
        icao_koodi = input("Kerro lentokentän ICAO-koodi: ")
        kentta = input("Kerro lentokentän nimi: ")
        kentat[icao_koodi]=kentta
    elif toiminto == "haku":
        haettava = input("Hae kenttää ICAO-koodilla: ")
        if haettava in kentat:
            print(f"Koodia vastaava kenttä on {kentat[haettava]}")
        else:
            print("Koodia vastaavaa kenttää ei löydy!")
    toiminto = input("Kirjoita toiminto: 'uusi tieto', 'haku' tai 'lopeta': ")


print(kentat)
print("Kiitos käynnistä!")
