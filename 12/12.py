# -*- coding: utf-8 -*-
# Python 3.8.6

a = "y"
n = 1

while (a == "y"):
    print("Token number ", n, " may come in!\n", sep = "", end = "")
    a = input("Continue? (y/n) ")
    while (a != "y" and a != "n"):
        print("Choose between y and n! ", sep = "", end = "")
        a = input("Continue? (y/n) ")
    n = n+1

print("That's it for the day!\n", sep = "", end = "")

# The for loop assigns a new value to x every time, but nothing of this sort happens in the while loop.
# The for loop iterates through iterable collections, whereas the while loop simply loops until the specified condition is false.
# The for loop is used when the number of iterations is definite.
# The for loop is used when an operation is to be done on each member of a sequence, in order.