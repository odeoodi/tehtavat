# tee ratkaisu tänne


def shakkilauta(ruudut):
    for a in range(ruudut):
        if a % 2 == 0:
            for i in range(ruudut):
                if i % 2 == 0:
                    print(1, end="")
                else:
                    print(0, end="")
        else:
            for i in range(ruudut):
                if i % 2 != 0:
                    print(1, end="")
                else:
                    print(0, end="")

        print()


shakkilauta(6)