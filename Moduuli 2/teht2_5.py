leiviska = float(input("Anna leiviskät: "))
naula = float(input("Anna naulat: "))
luoti = float(input("Anna luodit: "))

luotigramma = 13.3*luoti
naulagramma = naula*32*13.3
leiviskagramma = leiviska*20*32*13.3

massagramma = luotigramma + naulagramma + leiviskagramma

kilot = massagramma//1000

grammat = massagramma%1000

print(f"Massa nykymittojen mukaan:\n {kilot} kilogrammaa ja {grammat:.0f} grammaa.")