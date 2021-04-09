# -*- coding: utf-8 -*-
# Python 3.8.6

a = input().split(",")

numberOfSnakes = 0; numberOfLadders = 0

for x in a:

    b = x.split(":")
    startOfToken = int(b[0].strip()); endOfToken = int(b[1].strip())

    if startOfToken < endOfToken:
        numberOfLadders = numberOfLadders+1
    elif startOfToken > endOfToken:
        numberOfSnakes = numberOfSnakes+1

print(numberOfSnakes, numberOfLadders)





# /* Trivia
#
#  * string.strip(characters) removes the specified leading and trailing
#    characters from the specified string, and returns the trimmed string. If no
#    characters are specified, then all of the leading and trailing whitespaces
#    are removed.
#    [The characters need to be written together as a single string]
#  * int(), float(), etc. also trim the leading and trailing whitespaces.
#
#  */