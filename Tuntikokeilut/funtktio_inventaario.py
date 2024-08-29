def inventaario(tavarat):
    print("Sinulla on seuraavat tavarat:")
    for t in tavarat:
        print(f"- {t}")
    # jos haluat tyhjentää listan välissä:
    #tavarat.clear()
    return

reppu = ["vesipullo", "veitsi", "taskulamppu"]
inventaario(reppu)
reppu.append("kynä")
inventaario(reppu)