while True:
    user_input = input("Anna numero 1 ja 10 väliltä: ")
    if user_input.isdigit() and 1 <= int(user_input) <= 10:
        break
    print("Virheellinen syöte, yritä uudelleen.")
