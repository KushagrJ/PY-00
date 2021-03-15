# -*- coding: utf-8 -*-
# Python 3.8.6

a = "y"
n = 1

while a == "y":
    print("Token number", n, "may come in!")
    a = input("Continue? (y/n) ")
    while a != "y" and a != "n":
        print("Choose between y and n! ", end = "")
        a = input("Continue? (y/n) ")
    n = n+1

print("That's it for the day!")





# /* Trivia
#
#  * The for loop assigns a new value to x every time, but nothing of this sort happens in the while loop.
#  * The for loop iterates through iterable collections (strings, lists, tuples, etc.), whereas the while loop simply
#    loops until the specified condition is false - This should be used to know whether to use the for loop or the while
#    loop.
#  * The for loop is used when the number of iterations is definite.
#  * The for loop is used when an operation is to be done on each member of an iterable, in order.
#
#  * An iterable is anything that can be looped over with a for loop. Sequences (strings, lists, tuples, etc.), sets,
#    dictionaries, etc. are iterables.
#  * Sequences are iterables having a specific set of features, such as indexing via a range of numbers, slicing, etc.
#  * Strings and tuples are immutable sequences, i.e. they cannot be modified in place.
#
#  */