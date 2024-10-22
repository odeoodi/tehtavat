kuha = float(input("Anna kuhan mitta (cm): "))

puuttuu = 37-kuha

if kuha < 37:
    print(f"Päästä kuha vapaaksi! Alamitasta puuttuu {puuttuu}cm.")
elif kuha > 103:
    print("Nyt en usko...")
else:
    print("Hyvä kuha :)")