# -*- coding: utf-8 -*-
# Python 3.8.6

import string

cipherKey = {}

for x in range(len(string.ascii_letters)):
    cipherKey[string.ascii_letters[x]] = string.ascii_letters[x-5]

with open("python.txt") as p:
    q = p.read(); q = list(q)
    for y in range(len(q)):
        if q[y] in cipherKey:
            q[y] = cipherKey[q[y]]
        else:
            pass
    r = "".join(q)

print(r)





# /* Trivia
#
#  * variableName = {} declares a dictionary. It is used to store data in
#    'key:value' pairs.
#  * Dictionaries are insertion ordered, which means that they are ordered
#    according to the order in which items are added.
#  * Dictionaries don't resize when items are removed. They re-calculate when
#    re-insertion is done.
#  * dictionaryName[key] = value adds an item to the specified dictionary with
#    the specified key. If an item already exists with the specified key, then
#    its value gets changed.
#  * dictionaryName[key] returns the value with the specified key.
#  * dictionaryName.keys() returns the keys of the specified dictionary
#    (for eg., dict_keys([key1,key2,...])). list(dictionaryName.keys()) returns
#    the keys of the specified dictionary as a list (for eg., [key1,key2,...]).
#  * dictionaryName.values() returns the values of the specified dictionary
#    (for eg., dict_values([value1,value2,...])). list(dictionaryName.values())
#    returns the values of the specified dictionary as a list (for eg.,
#    [value1,value2,...]).
#  * dictionaryName.items() returns the items of the specified dictionary
#    (for eg., dict_items([(key1,value1),(key2,value2),...])).
#    list(dictionaryName.values()) returns the values of the specified
#    dictionary as a list (for eg., [(key1,value1),(key2,value2),...]).
#  * for x in dictionaryName: iterates over the keys of the specified
#    dictionary. To iterate over the specified dictionary's values,
#    for x in dictionaryName.values(): should be used.
#  * del dictionaryName[key] / dictionaryName.pop(key) removes the item with the
#    specified key from the specified dictionary. pop returns the value of the
#    deleted item, whereas del does not.
#  * dictionaryName.clear() empties the specified dictionary.
#
#  * a = "kushagr"; a.replace("k", "K") returns 'Kushagr'
#  * a = "Kushagr"; a.upper() returns 'KUSHAGR'
#  * a = "Kushagr"; a.lower() returns 'kushagr'
#  * a = "Kushagr"; a.swapcase() returns 'kUSHAGR'
#
#  * string.isalpha() returns True if all the characters in the specified
#    string are alphabetical (i.e. a-z or A-Z).
#
#  * 'if x is None' is better than 'if not x'.
#
#  */