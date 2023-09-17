#!/usr/bin/python3

"""This is python function pract"""

def repeat(text, repetitions=5):
   return f"{text}\n" * repetitions

text = input("Enter some text:  ")
print(repeat (text))
