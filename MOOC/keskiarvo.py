# Ohjelmointi 1 arvosana:

matikka = int(input("Matikan arvosana: "))
python = int(input("Pythonin arvosana: "))
viestinta = int(input("Viestinnän arvosana: "))
projekti = int(input("Projektin arvosana: "))

arvosana = (matikka+python+viestinta+projekti)/4

print(f"Sait kurssista {arvosana}")