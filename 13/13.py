# -*- coding: utf-8 -*-
# Python 3.8.6

shoppingList = ["1 Packet Bread", "1 Packet Butter", "1 Litre Milk"]


print(shoppingList)
print()


for x in shoppingList:
    print(x)

print()


shoppingList.append("250 Grams Curd")

print(shoppingList)
print()


shoppingList.insert(0, "500 Millilitres Oil")
shoppingList.insert(3, "12 Eggs")

for x in shoppingList:
    print(x)





# /* Trivia
#
#  * variableName = [] declares a list.
#  * shoppingList.append("Name of Item") adds an item at the end of shoppingList.
#  * shoppingList.insert(unsignedInt, "Name of Item") adds an item at the index specified by unsignedInt.
#  * shoppintList[unsignedInt] = "Name of New Item" changes the item at the index specified by unsignedInt.
#  * for x in shoppingList: can be written as for x in ["1 Packet Bread", "1 Packet Butter", "1 Litre Milk"]: as well.
#    [Similarly for other sequences]
#  * list(iterableName) returns a list containing all of the elements in the specified iterable.
#
#  */