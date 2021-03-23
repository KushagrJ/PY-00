# -*- coding: utf-8 -*-
# Python 3.8.6

import random, string


def main():

    player1, player2 = get_the_names_of_the_players()

    a = "Y"
    playerWhoseTurn = 1
    pointsOf1 = 0
    pointsOf2 = 0

    while a != "N":

        chosenMovie, hiddenMovie = get_a_movie_name_from_the_list_of_movies()

        if playerWhoseTurn == 1:
            pointsOf1 = play(chosenMovie, hiddenMovie, player1, pointsOf1)
            a, playerWhoseTurn = ask_whether_to_continue(playerWhoseTurn)
        else:
            pointsOf2 = play(chosenMovie, hiddenMovie, player2, pointsOf2)
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

    print("\n")

    return player1, player2


def get_a_movie_name_from_the_list_of_movies():

    listOfMovies = ["THE AVENGERS", "CAPTAIN AMERICA THE WINTER SOLDIER",
                    "AVENGERS AGE OF ULTRON", "CAPTAIN AMERICA CIVIL WAR",
                    "SPIDER MAN HOMECOMING", "THOR RAGNAROK",
                    "AVENGERS INFINITY WAR", "AVENGERS ENDGAME",
                    "SPIDER MAN FAR FROM HOME", "MAN OF STEEL",
                    "WONDER WOMAN", "AQUAMAN", "SHAZAM", "JUSTICE LEAGUE"]

    chosenMovie = random.choice(listOfMovies)

    hiddenMovieAsAList = []

    for x in chosenMovie:
        if x == " ":
            hiddenMovieAsAList.append(x)
        else:
            hiddenMovieAsAList.append("*")

    hiddenMovie = "".join(hiddenMovieAsAList)

    return chosenMovie, hiddenMovie


def play(chosenMovie, hiddenMovie, player, points):

    guessedMovie = hiddenMovie
    incorrectGuessesLeft = 5

    print(player, ", guess the movie name :-\n", sep = "")

    while guessedMovie != chosenMovie and incorrectGuessesLeft != 0:

        print(guessedMovie, " (Incorrect letter guesses left = ",
              incorrectGuessesLeft, ")", sep = "")

        # To allow only 1 or 2 as input.
        answer1 = "0"
        while answer1 not in ["1","2"]:
            answer1 = input("Enter 1 to guess a letter or 2 to guess the "
                            "movie: ")
        answer1 = int(answer1)

        if answer1 == 1:

            # To allow only uppercase letters as input.
            answer2 = "0"
            while answer2 not in string.ascii_uppercase or answer2 == "":
                answer2 = input("Enter the letter (in uppercase): ")

            if answer2 in chosenMovie:
                print("Correct guess!\n")
                hiddenMovieAsAList = []
                for x in chosenMovie:
                    if answer2 == x:
                        hiddenMovieAsAList.append(answer2)
                    elif x in guessedMovie or x == " ":
                        hiddenMovieAsAList.append(x)
                    else:
                        hiddenMovieAsAList.append("*")
                guessedMovie = "".join(hiddenMovieAsAList)

            else:
                print("Sorry, better luck next time!\n")
                incorrectGuessesLeft = incorrectGuessesLeft-1

        else:

            answer2 = input("Enter the movie name (in uppercase): ")

            if answer2 == chosenMovie:
                guessedMovie = chosenMovie
                print()

            else:
                print("Sorry, better luck next time!\n")
                incorrectGuessesLeft = 0

    if guessedMovie == chosenMovie:
        points = points+1
        print("Cheers!", chosenMovie, "is a great movie!")
        print(player, "'s Score = ", points, sep = "")
    else: # incorrectGuessesLeft == 0
        print("The name of the movie is ", chosenMovie, "!", sep = "")
        print(player, "'s Score = ", points, sep = "")

    return points


def ask_whether_to_continue(playerWhoseTurn):

    # To allow only Y or N as input.
    a = "0"
    while a not in ["Y", "N"]:
        a = input("Continue? (Y/N) ")

    if a == "Y":
        if (playerWhoseTurn == 1):
            playerWhoseTurn = 2
        else:
            playerWhoseTurn = 1
        print("\n")
    else:
        print("\n")

    return a, playerWhoseTurn


main()