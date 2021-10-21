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





# /* Trivia - 31.py
#
#  * File formats such as mp3, aac, etc. aren't recognised by Python's
#    SpeechRecognition.
#  * An internet connection is required for SpeechRecognition to work.
#
#  * The try block lets the user test a block of code for errors.
#    The except block lets the user handle an error.
#
#  * End of Trivia */
