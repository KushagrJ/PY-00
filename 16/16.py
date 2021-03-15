# -*- coding: utf-8 -*-
# Python 3.8.6

def main():

    list = [100, 300, 150, 250, 125, 275, 175, 225, 190, 210, 180, 220, 195,
            205, 170, 230, 165, 235, 115, 285, 120, 280, 140, 260, 145, 255,
            196, 204, 187, 213, 181, 219, 156, 210, 203, 212, 193, 211, 182]

    list.sort()

    numberOfItems = len(list)

    print_the_list_in_ascending_order(list, numberOfItems)

    trimmedMean1 = get_the_trimmed_mean_using_calculation(list, numberOfItems)

    trimmedMean2 = get_the_trimmed_mean_using_scipy(list)

    if trimmedMean1 == trimmedMean2:
        percentSign = "%"
        print("The 10", percentSign, " trimmed mean of the given data is ",
              trimmedMean1, sep = "")
    else:
        print("There is some error in your calculation!")


def print_the_list_in_ascending_order(list, numberOfItems):

    print("The given data (in ascending order) is :-")

    for x in range(numberOfItems):                                                  # To print list like 1, 2, 3, 4 & 5
        if (x+1 == numberOfItems):                                                  # instead of like [1, 2, 3, 4, 5].
            print(list[x], "\n")
        elif (x+2 == numberOfItems):
            print(list[x], end = " & ")
        else:
            print(list[x], end = ", ")


def get_the_trimmed_mean_using_calculation(list, numberOfItems):

    tenPercentItems = int(0.1*numberOfItems)

    trimmedList = list[tenPercentItems : numberOfItems-tenPercentItems]

    newNumberOfItems = numberOfItems-(2*tenPercentItems)

    sum = 0
    for x in trimmedList:
        sum = sum+x

    trimmedMean1 = sum/newNumberOfItems

    return trimmedMean1


def get_the_trimmed_mean_using_scipy(list):

    from scipy import stats

    trimmedMean2 = stats.trim_mean(list, 0.1)

    return trimmedMean2


main()





# /* Trivia
#
#  * The number of items to reject from either side to calculate the 10% trimmed mean is given by
#    max{n | n <= x, integer n}, where x is equal to 0.1*numberOfItems. This is also known as the floor function or the
#    greatest integer function.
#
#  */