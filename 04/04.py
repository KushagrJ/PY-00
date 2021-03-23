# -*- coding: utf-8 -*-
# Python 3.8.6

cost = input("Enter the cost of the product: Rs. ")
percentSign = "%"

cost = float(cost)

costAfterDiscount = 0.9*cost

print("The cost of the product after applying a 10", percentSign, " discount ",
      "is Rs. ", costAfterDiscount, sep = "")





# /* Trivia
#
#  * For numerical data types, it's better to specify int, float, etc. in order
#    to get the desired results.
#
#  * cost = float(input("Enter the cost of the product: ")) is the same as
#    cost = input("Enter the cost of the product: "); cost = float(cost)
#  * percentSign = "%" is used to print %.
#
#  */