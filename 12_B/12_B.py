# -*- coding: utf-8 -*-
# Python 3.8.6

a = "y"
n = 1


while a != "n":

    if a == "y":
        print("Token number", n, "may come in!")
        a = input("Continue? (y/n) ")
        n = n+1

    else:
        print("Choose between y and n! ", end = "")
        a = input("Continue? (y/n) ")


print("That's it for the day!")