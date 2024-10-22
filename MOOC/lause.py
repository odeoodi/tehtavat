sana = input("Anna sana: ")

lause = ""
while sana != "loppu":
    lause += sana + " "
    sana1 = input("Anna sana: ")
    if sana == sana1:
        break
    sana = sana1
print(lause)