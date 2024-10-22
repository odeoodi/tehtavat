"""
pseudo code for one round:

intro()


while money > 0 or right_answers in accusations:
    print(check_money())

    round = input("What would you like to do: ")
    print('See the options by typing "help"')

    if round == "help":
        print(help())
    elif round == "accuse":
        accusation = input("Make your accusations: ")
        print(check_if_correct())
    elif round == "fly":
        destination = input("Where would you like to travel: ")
        fly()
    elif round == "check accusations":
        print(accusations)
    elif round == "end game":
        end_game()

if money == 0:
    print("you lost the game")
else:
    print("you won")
"""