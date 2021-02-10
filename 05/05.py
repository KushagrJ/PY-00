# -*- coding: utf-8 -*-
# Python 3.8.6

cost = float(input("Enter the cost of the product: Rs. "))
percentSign = "%"

costForProfit = 1.15 * cost

print("You should sell this product for Rs. ", costForProfit, " to earn a 15", percentSign, " profit\n", sep = "", end = "")