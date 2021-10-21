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





# /* Trivia - 12-A.py
#
#  * The for loop assigns a new value to x every time, but nothing of this sort
#    happens in the while loop.
#  * The for loop iterates through iterable collections (strings, lists, tuples,
#    etc.), whereas the while loop simply loops until the specified condition is
#    false - This should be used to know whether to use the for loop or the
#    while loop.
#  * The for loop is used when the number of iterations is definite.
#  * The for loop is used when an operation is to be done on each member of an
#    iterable, in order.
#
#  * break terminates the current loop (for/while) and resumes execution at the
#    next statement.
#    [For nested loops, break only terminates the loop it is placed in]
#    continue rejects all the remaining statements in the current iteration of
#    a loop (for/while) and moves the control back to the top of the loop.
#    [For nested loops, continue only rejects the remaining statements of the
#    loop it is placed in, and moves the control back to the top of that loop]
#    pass is a null operation. Nothing happens when it executes.
#
#  * An iterable is anything that can be looped over with a for loop. Sequences
#    (strings, lists, tuples, etc.), sets, dictionaries, etc. are iterables.
#  * Sequences are iterables having a specific set of features, such as indexing
#    via a range of numbers, slicing, etc.
#  * Strings and tuples are immutable sequences, i.e. they cannot be modified in
#    place.
#  * Sequences can be concatenated with +.
#  * Sequences can be repeated a positiveInt number of times with *.
#  * The 'in' operator checks whether the specified value is an element of the
#    specified sequence.
#
#  * End of Trivia */
