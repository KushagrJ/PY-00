# -*- coding: utf-8 -*-
# Python 3.8.6

shoppingList = ["1 Packet Bread", "1 Packet Butter", "1 Litre Milk"]


print(shoppingList, "\n\n", sep = "", end = "")


for x in shoppingList:
    print(x, "\n", sep = "", end = "")

print("\n", sep = "", end = "")


shoppingList.append("250 Grams Curd")

print(shoppingList, "\n\n", sep = "", end = "")


shoppingList.insert(0, "500 Millilitres Oil")
shoppingList.insert(3, "12 Eggs")

for x in shoppingList:
    print(x, "\n", sep = "", end = "")





# /* Trivia
#
#  * variableName = [] declares a data structure called list.
#  * shoppingList.append("Name of Item") adds an item to the end of shoppingList.
#  * shoppingList.insert(unsignedInt, "Name of Item") adds an item to the position specified by unsignedInt.
#
#  */