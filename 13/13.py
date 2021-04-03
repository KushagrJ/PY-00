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
#  * shoppingList.append(item) adds the specified item at the end of
#    shoppingList.
#  * shoppingList.insert(index, item) adds the specified item at the specified
#    index.
#  * shoppingList[index] returns the item at the specified index.
#  * shoppingList.remove(item) removes the specified item from shoppingList.
#    Also, shoppingList.remove(shoppingList[index]) works as well.
#  * shoppingList[index] = item changes the item at the specified index.
#  * for x in shoppingList: can be written as
#    for x in ["1 Packet Bread", "1 Packet Butter", "1 Litre Milk"]: as well.
#    [Similarly for other sequences]
#  * list(iterableName) returns a list containing all of the elements in the
#    specified iterable.
#
#  * Negative indexing starts from where a sequence ends. So, [-1] corresponds
#    to the last element of a sequence, [-2] corresponds to the second last
#    element of a sequence, and so on.
#
#  */