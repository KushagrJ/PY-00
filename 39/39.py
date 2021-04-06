# -*- coding: utf-8 -*-
# Python 3.8.6

import numpy


def main():

    playingBoard = numpy.array([["-", "-", "-"]]*3)

    a = "y"
    player = "X"
    while "-" in playingBoard and a == "y":
        playingBoard, player, a = play(playingBoard, player, a)


def play(playingBoard, player, a):

    print(player, ", choose a position :-", sep = "")
    row = 0; column = 0
    while (row not in ["1","2","3"]) or (column not in ["1","2","3"]):
        row = input("Row (1/2/3): "); column = input("Column (1/2/3): ")
    row = int(row)-1; column = int(column)-1

    while playingBoard[row, column] != "-":
        print("Position already occupied! Choose another position!\n")
        row = 0; column = 0
        while (row not in ["1","2","3"]) or (column not in ["1","2","3"]):
            row = input("Row (1/2/3): "); column = input("Column (1/2/3): ")
        row = int(row)-1; column = int(column)-1

    playingBoard[row, column] = player
    print(); print(numpy.matrix(playingBoard), "\n")

    if player == "X":
        player = "O"
    else:
        player = "X"

    a = check_whether_the_player_has_won("X", playingBoard, a)

    if a == "y":
        a = check_whether_the_player_has_won("O", playingBoard, a)

    return playingBoard, player, a


def check_whether_the_player_has_won(player, playingBoard, a):

    while True:

        # To check the rows.
        for r in range(3):
            count = 0
            for c in range(3):
                if playingBoard[r,c] == player:
                    count = count+1
            if count == 3:
                print("Congratulations!", player, "has won the game!"); a = "n"
                break

        # To check the columns.
        for c in range(3):
            count = 0
            for r in range(3):
                if playingBoard[r,c] == player:
                    count = count+1
            if count == 3:
                print("Congratulations!", player, "has won the game!"); a = "n"
                break

        # To check the first diagonal.
        count = 0
        for r in range(3):
            c = r
            if playingBoard[r,c] == player:
                count = count+1
            if count == 3:
                print("Congratulations!", player, "has won the game!"); a = "n"
                break

        # To check the second diagonal.
        count = 0
        for r in range(2,-1,-1):
            c = 2-r
            if playingBoard[r,c] == player:
                count = count+1
            if count == 3:
                print("Congratulations!", player, "has won the game!"); a = "n"
                break

        if "-" not in playingBoard:
            print("The game has ended in a draw!"); a = "n"

        break

    return a


main()





# /* Trivia
#
#  * Lists within a list can also be used instead of numpy arrays.
#  * Numpy only supports rectangular and homogeneous arrays, as opposed to
#    lists.
#  * For numpy arrays, arr[i][j] and arr[i,j] both can be used to access an
#    element. For lists within a list, arr[i,j] doesn't work.
#
#  * a = [[1,2,3],[4,5,6],[7,8,9]]; 1 in a returns False
#  * import numpy; a = numpy.array([[1,2,3],[4,5,6],[7,8,9]]); 1 in a returns
#    true
#
#  * while row or column not in ["1","2","3"]: doesn't work.
#
#  */