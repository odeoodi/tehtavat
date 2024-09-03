import random
def heita():
    eka, toka = random.randint(1,6),random.randint(1,6)
    return eka, toka

noppa1, noppa2 = heita()

print(f"Nopista tuli {noppa1} ja {noppa2}.")