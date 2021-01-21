import random

min = 1
max = 6

dicenum = 0
roll_again = "no"

while roll_again == "no" or roll_again == "n":
    print("\n")
    dicenum = int(input("How many dice would you like to roll?"))
    print("\n")
    roll_again = "yes"

    while roll_again == "yes" or roll_again == "y":
        print("Rolling", dicenum, "dice...")
        print("The values are....")
        for i in range(dicenum):
            print(random.randint(min, max), sep='', end='-', flush=True)
            roll_again = "no"
