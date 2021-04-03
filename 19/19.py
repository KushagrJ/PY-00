# -*- coding: utf-8 -*-
# Python 3.8.6

import random


with open("data.txt") as data:

    a = data.read()
    b = list(a)
    numberOfIterations = 0

    while b.count("0") != 0:

        numberOfIterations = numberOfIterations+1

        x = random.randrange(0, len(b))

        if b[x] == "0":
            b[x] = "1"
        else:
            pass

    c = "".join(b)


print("Converting", a, "into", c, "took", numberOfIterations, "iterations")





# /* Trivia
#
#  * open("fileName", "mode") returns the file object (such as a text file)
#    specified by fileName in the specified mode. The mode can be r (read only),
#    w (write only), r+ (read and write) or a (append). The default mode is r.
#  * It is good practice to use the 'with' keyword when dealing with file
#    objects, as it closes the file properly after its work is finished.
#  * fileName.read() reads and returns the entire contents of the specified file
#    object.
#  * fileName.write(string) writes the contents of the string to the specified
#    file object. If the file object is opened in "w" or "r+" mode, then any
#    existing file with the same name will be erased and the string will be
#    written to a new file with the same name. To add data to an existing file,
#    it should be opened in "a" mode.
#  * fileName.close() closes the specified file object. This is not required if
#    'with' is used.
#
#  * random.randint(int1, int2) returns a randomly selected integer from the
#    range int1 to int2, including them both.
#  * random.randrange(int1, int2+1, positiveInt) returns a randomly selected
#    integer from the range int1 to int2, including them both. positiveInt sets
#    the incrementation. The default values of int1 and positiveInt are 0 and 1,
#    respectively.
#  * random.random() returns a randomly selected floating-point value belonging
#    to [0, 1).
#
#  */