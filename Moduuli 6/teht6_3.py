#Kirjoita funktio, joka saa parametrinaan bensiinin määrän Yhdysvaltain nestegallonoina ja
# palauttaa paluuarvonaan vastaavan litramäärän. Kirjoita pääohjelma, joka kysyy gallonamäärän käyttäjältä
# ja muuntaa sen litroiksi. Muunnos on tehtävä aliohjelmaa hyödyntäen. Muuntamista jatketaan siihen saakka,
# kunnes käyttäjä syöttää negatiivisen gallonamäärän.
#Yksi gallona on 3,785 litraa.

def bensa(gallonat):
    litrat = gallonat*3.785
    return litrat

gallonat = float(input("Anna gallonat: "))
tulos = bensa(gallonat)
while gallonat >= 0:
    print(f"{gallonat} gallonaa on {tulos} litraa.")
    gallonat = float(input("Anna gallonat: "))
    if gallonat < 0:
        print("Anna vain positiivisia lukuja.")

