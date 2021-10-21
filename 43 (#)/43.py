# -*- coding: utf-8 -*-
# Python 3.8.6

string1 = input(); string2 = input()
listOfString1 = []; listOfString2 = []

for x in string1:
    if x.isalpha():
        listOfString1.append(x.lower())

for y in string2:
    if y.isalpha():
        listOfString2.append(y.lower())

listOfString1.sort(); listOfString2.sort()

if len(listOfString1) != len(listOfString2):
    print("No")
else:
    for z in range(len(listOfString1)):
        if listOfString1[z] != listOfString2[z]:
            print("No"); break
    else:
        print("Yes")





# /* Trivia - 43.py
#
#  * for-else statements :-
#    (a) if break is encountered in the for loop or if the body of the for loop
#        raises an exception, then the else part will not be called.
#    (b) if break is not encountered in the for loop or if the for loop does not
#        iterate at all, then the else part will be called.
#
#  * End of Trivia */
