# -*- coding: utf-8 -*-
# Python 3.8.6

n = 0
while n not in [1,3,5,7,9]:
    n = int(input("Enter the order of the desired magic square (1/3/5/7/9): "))
print()


# To add zeroes to every position.
magicSquare = [[0 for x in range(n)] for y in range(n)]


number =  1
i = int(n/2); j = n-1

while number < (n*n)+1:

    magicSquare[i][j] = number

    # In case there is already a number at the calculated position.
    a = i; b = j

    i = i-1; j = j+1

    if i == -1:
        i = n-1
    else:
        pass

    if j == n:
        j = 0
    else:
        pass

    if magicSquare[i][j] != 0:
        i = a
        j = b-1
    else:
        pass

    number = number+1


for i in magicSquare:

    for j in i:

        if j < 10:
            print(0, j, sep = "", end = " ")
        else:
            print(j, end = " ")

    print()





# /* Trivia
#
#  * A square array of numbers, usually distinct positive integers, is called a
#    magic square if the sums of the numbers in each row, each column and both
#    main diagonals are the same. The order of the magic square is the number of
#    integers along one side (n) and the constant sum is called the magic
#    constant (M).
#  * An algorithm for the construction of odd-ordered magic squares with the
#    numbers being 1,2,3,4,5,...,n^2 is as follows:
#    (1) The position of 1 is (int(n/2), n-1).
#    (2) If (i,j) is the position of a number, then the position of the next
#        number is given by (i-1, j+1) (with appropriate wrapping, i.e. row -1
#        becomes row n-1 and column n becomes column 0), unless
#        (a) there is already a number at the calculated position, in which case
#            the position of the next number is given by (i, j-1).
#        (b) the calculated position comes out to be (-1, n), in which case the
#            position of the next number is given by (0, n-2).
#            [This is probably redundant]
#    [In simple words, starting with 1, numbers are filled diagonally up and
#     right, with appropriate wrapping. If a filled position is encountered,
#     then the position of the next number becomes immediately left to that of
#     the current number.]
#
#  * 2-dimensional arrays/lists are basically lists within a list. The multiple
#    lists within a larger list can be thought of as rows, with their elements'
#    indices representing the column numbers.
#    For eg., list = [[1,2,3],[4,5,6],[7,8,9]]; list[1][2] returns 6.
#
#  */