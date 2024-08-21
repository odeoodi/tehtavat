sukupuoli = input("Kerro biologinen sukupuoli: ")
hemo = float(input("Hemoglobiinisi: "))

if (sukupuoli == "nainen" and 117 <= hemo <= 175) or (sukupuoli == "mies" and 134 <= hemo <= 195):
    print("Hemoglobiinisi on normaali.")
elif (sukupuoli == "nainen" and hemo < 117) or (sukupuoli == "mies" and hemo < 134):
    print("Hemoglobiinisi on alhainen.")
elif (sukupuoli == "nainen" and hemo > 175) or (sukupuoli == mies and hemo > 195):
    print("Hemogloniinisi on korkea.")

