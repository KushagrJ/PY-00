# -*- coding: utf-8 -*-
# Python 3.8.6

import random


def main():

    player1, player2 = get_the_names_of_the_players()

    a = "y"
    playerWhoseTurn = 1
    pointsOf1 = 0
    pointsOf2 = 0

    while a != "n":

        chosenWord, jumbledWord = get_a_jumbled_word_from_the_list_of_words()

        if playerWhoseTurn == 1:
            pointsOf1 = play(chosenWord, jumbledWord, player1, pointsOf1)
            a, playerWhoseTurn = ask_whether_to_continue(playerWhoseTurn)
        else:
            pointsOf2 = play(chosenWord, jumbledWord, player2, pointsOf2)
            a, playerWhoseTurn = ask_whether_to_continue(playerWhoseTurn)

    if pointsOf1 > pointsOf2:
        print(player1, "won the game!")
    elif pointsOf2 > pointsOf1:
        print(player2, "won the game!")
    else:
        print("The game has ended in a tie!")


def get_the_names_of_the_players():

    player1 = input("Enter the name of player 1: ")

    player2 = input("Enter the name of player 2: ")

    print()

    return player1, player2


def get_a_jumbled_word_from_the_list_of_words():

    listOfWords = ["rainbow", "computer", "science", "programming", "board",
                   "mathematics", "player", "condition", "reverse", "water"]

    chosenWord = random.choice(listOfWords)

    jumbledWord = "".join(random.sample(chosenWord, len(chosenWord)))

    return chosenWord, jumbledWord


def play(chosenWord, jumbledWord, player, points):

    print(player, ", unjumble ", jumbledWord, ": ", sep = "", end = "")

    answer = input()

    if answer == chosenWord:
        points = points+1
        print("Correct!")
        print(player, "'s Score = ", points, sep = "")
    else:
        print("Sorry, better luck next time!")
        print(player, "'s Score = ", points, sep = "")

    return points


def ask_whether_to_continue(playerWhoseTurn):

    a = input("Continue? (y/n) ")

    while a != "y" and a != "n":
        a = input("Continue? (y/n) ")

    if a == "y":
        if (playerWhoseTurn == 1):
            playerWhoseTurn = 2
        else:
            playerWhoseTurn = 1
        print()
    else:
        print()

    return a, playerWhoseTurn


main()





# /* Trivia
#
#  * random.choice(sequenceName) returns a randomly selected element from the
#    specified sequence.
#  * random.sample(sequenceName, positiveInt) returns a list with a random
#    selection of the number of elements specified by positiveInt from the
#    specified sequence.
#  * "separator".join(iterableName) returns a string after taking all of the
#    elements in the specified iterable and joining them into a single string,
#    with the specified separator separating the elements.
#
#  */