# -*- coding: utf-8 -*-
# Python 3.8.6

def main():

    print("Enter a list of integers: ", end = "")
    listOfNumbers = [int(i) for i in input().split()]
    listOfNumbers.sort()

    targetValue = int(input("Enter the integer to be searched: "))
    print()

    binary_search(listOfNumbers, targetValue)


def binary_search(listOfNumbers, targetValue):

    startingIndex = 0
    endingIndex = len(listOfNumbers)-1
    foundTargetValue = "n"

    while startingIndex <= endingIndex and foundTargetValue == "n":

        middle = int((startingIndex+endingIndex)//2)

        if targetValue == listOfNumbers[middle]:
            foundTargetValue = "y"
            print("The integer is located at index "+str(middle))
        else:
            if targetValue < listOfNumbers[middle]:
                endingIndex = middle-1
            else:
                startingIndex = middle+1


main()





# /* Trivia
#
#  * In linear search, the element to be found is searched sequentially in the
#    given list.
#  * Binary search works on sorted lists. It begins by comparing an element in
#    roughly the middle of the given list with the target value. If the target
#    value matches the element, its position in the list is returned. If the
#    target value is less than the element, the search continues in the lower
#    half of the list. If the target value is greater than the element, the
#    search continues in the upper half of the list. By doing this, the
#    algorithm eliminates the half in which the target value cannot lie in each
#    iteration.
#
#  * Recursion can also be used to perform binary search.
#
#  */