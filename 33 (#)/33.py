# -*- coding: utf-8 -*-
# Python 3.8.6

def main():

    print("Enter the integers to be sorted: ", end = "")
    a = [int(i) for i in input().split()]

    bubble_sort(a)


def bubble_sort(a):

    n = len(a)

    for x in range(1,n):

        for y in range(n-x):

            if a[y] > a[y+1]:
                temp = a[y]
                a[y] = a[y+1]
                a[y+1] = temp
            else:
                pass

    print("The sorted list is", a)


main()





# /* Trivia
#
#  * After every for x loop, the largest integer in that iteration gets shifted
#    to the desired place.
#
#  */