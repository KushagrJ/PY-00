# -*- coding: utf-8 -*-
# Python 3.8.6

encodedMessage = input()
encodedMessage = encodedMessage[::-1]

decodedMessage = ""

for x in encodedMessage:
    if x == "A":
        decodedMessage = decodedMessage+"X"
    elif x == "B":
        decodedMessage = decodedMessage+"Y"
    elif x == "C":
        decodedMessage = decodedMessage+"Z"
    else:
        decodedMessage = decodedMessage+chr(ord(x)-3)

print(decodedMessage)