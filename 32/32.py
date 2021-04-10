# -*- coding: utf-8 -*-
# Python 3.8.6

import random

numberOfWinsWithSwapping = 0
numberOfWinsWithoutSwapping = 0

for i in range(30):

    cups = ["Empty"]*3

    chocolateCupNumber = random.randrange(3)
    cups[chocolateCupNumber] = "Chocolate"
    cupNumbersOfEmptyCups = [x for x in range(3) if x != chocolateCupNumber]

    originalAnswer = 0
    while originalAnswer not in ["0","1","2"]:
        originalAnswer = input("Choose a cup number (0/1/2): ")
    originalAnswer = int(originalAnswer)

    cupNumberToShow = originalAnswer
    while cupNumberToShow == originalAnswer:
        cupNumberToShow = random.choice(cupNumbersOfEmptyCups)

    swap = 0
    while swap not in ["y", "n"]:
        print("Cup number", cupNumberToShow, "is empty. Would you like to",
              "change your answer? (y/n) ", end = "")
        swap = input()

    if swap == "y":
        if cups[originalAnswer] == "Chocolate":
            print("Sorry, better luck next time!")
        else:
            print("Congratulations! You won the chocolate!")
            numberOfWinsWithSwapping = numberOfWinsWithSwapping+1
    else:
        if cups[originalAnswer] == "Chocolate":
            print("Congratulations! You won the chocolate!")
            numberOfWinsWithoutSwapping = numberOfWinsWithoutSwapping+1
        else:
            print("Sorry, better luck next time!")

    print()

print("No. of wins with swapping =", numberOfWinsWithSwapping)
print("No. of wins without swapping =", numberOfWinsWithoutSwapping)





# /* Trivia
#
#  * The Monty Hall problem - https://www.youtube.com/watch?v=4Lb-6rxZxx0
#
#  */