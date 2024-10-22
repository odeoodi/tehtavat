sukupuoli = input("Kerro biologinen sukupuoli(M/N): ")
hemo = float(input("Hemoglobiinisi: "))

if (sukupuoli == "N" and 117 <= hemo <= 175) or (sukupuoli == "M" and 134 <= hemo <= 195):
    print("Hemoglobiinisi on normaali.")
elif (sukupuoli == "N" and hemo < 117) or (sukupuoli == "M" and hemo < 134):
    print("Hemoglobiinisi on alhainen.")
elif (sukupuoli == "N" and hemo > 175) or (sukupuoli == "M" and hemo > 195):
    print("Hemogloniinisi on korkea.")

