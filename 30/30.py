# -*- coding: utf-8 -*-
# Python 3.8.6

import speech_recognition as sr

SAMPLE_AUDIO = ("sample.wav")

r = sr.Recognizer()

with sr.AudioFile(SAMPLE_AUDIO) as sourceFile:
    audio = r.record(sourceFile)

try:
    print("The audio file says that", r.recognize_google(audio))
except sr.UnknownValueError:
    print("Google's Speech Recognition couldn't understand the audio file")
except sr.RequestError:
    print("Couldn't get the results from Google's Speech Recognition")





# /* Trivia
#
#  * File formats such as mp3, aac, etc. aren't recognised by Python's
#    SpeechRecognition.
#  * An internet connection is required for SpeechRecognition to work.
#
#  * The try block lets the user test a block of code for errors.
#    The except block lets the user handle an error.
#
#  */





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
#    specified key from the specified dictionary.
#  * dictionaryName.clear() empties the specified dictionary.
#
#  */