# -*- coding: utf-8 -*-
# Python 3.8.6

import random

print("Player 1 (User) vs. Player 2 (Python)")
print("0 = Rock, 1 = Paper and 2 = Scissors\n")

p1 = "0"
while p1 not in ["1", "2", "3"]:
    p1 = input("Player 1, enter your choice: ")
p1 = int(p1)
p2 = random.randrange(1,4)
winner = (p1-p2)%3

if p1 == p2:
    print("Draw!")
else:
    print("Player", winner, "wins!")





# /* Trivia
#
#  * For two users to play this game, a few modifications will be required to
#    ensure no cheating, such as making different assignments for each player,
#    making each player enter a long string of numbers out of which a specific
#    index will contain the player's choice, etc.
#    For eg., Each player will enter a 10-digit string (answer1 and answer2).
#             Player 1's answer = answer1[3].
#             Player 1's answer = answer2[7].
#             For Player 1, 0/3/6/9 will correspond to Rock, 1/4/7 will
#             correspond to Paper and 2/5/8 will correspond to Scissors.
#             For Player 2, 0/3/6/9 will correspond to Paper, 1/4/7 will
#             correspond to Rock and 2/5/8 will correspond to Scissors.
#
#  */