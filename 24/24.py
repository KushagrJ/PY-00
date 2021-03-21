# -*- coding: utf-8 -*-
# Python 3.8.6

import string, random

letters = list(string.ascii_letters)

list1 = [0]*5; list2 = [0]*5

positionInList1 = random.randrange(0,5); positionInList2 = random.randrange(0,5)

sameLetter = random.choice(letters); letters.remove(sameLetter)

if positionInList1 == positionInList2:
    list1[positionInList1] = sameLetter; list2[positionInList2] = sameLetter
else:
    list1[positionInList1] = sameLetter; list2[positionInList2] = sameLetter
    list1[positionInList2] = random.choice(letters)
    letters.remove(list1[positionInList2])
    list2[positionInList1] = random.choice(letters)
    letters.remove(list2[positionInList1])

i = 0
while i < 5:
    if i != positionInList1 and i != positionInList2:
        letterForList1 = random.choice(letters); letters.remove(letterForList1)
        letterForList2 = random.choice(letters); letters.remove(letterForList2)
        list1[i] = letterForList1
        list2[i] = letterForList2
    i = i+1

print("List 1: ", list1); print("List 2: ", list2); print()

answer = input("Enter the common letter: ")
if answer == sameLetter:
    print("Correct!")
else:
    print("Sorry, better luck next time!")





# /* Trivia
#
#  * import string; string.ascii_letters returns
#    'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
#
#  */