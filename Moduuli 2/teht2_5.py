leiviska = float(input("Anna leiviskät: "))
naula = float(input("Anna naulat: "))
luoti = float(input("Anna luodit: "))

luotigramma = 13.3*luoti
naulagramma = naula*32*13.3
leiviskagramma = leiviska*20*32*13.3

massagramma = luotigramma + naulagramma + leiviskagramma



print(f"Massa nykymittojen mukaan {kilot} kilogrammaa ja {grammat} grammaa.")