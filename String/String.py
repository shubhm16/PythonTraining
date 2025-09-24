# -*- coding: utf-8 -*-
"""
Created on Wed Sep 24 11:22:17 2025

@author: shubh
"""

s1 = 'Shubham'  # single quote
s2 = "Shubham"  # double quote
print(s1)
print(s2)

'Multi lines string'
s = """I am Learning
Python String """
print(s)

s = '''I'm a 
Shubham'''
print(s)

"String Slicing"

s = "ShubhamPythonTraing"
print(s[1:4])    # characters from index 1 to 3
print(s[:3])     # from start to index 2
print(s[3:])     # from index 3 to end
print(s[::-1])   # reverse string

'String Iteration'
s = "Python"
for char in s:
    print(char)
    
'String Immutability'
s = "PythonTrainingString"
s = "G" + s[1:]   # create new string
print(s)   

'Deleting string'
s = "Game"
del s

'Updating a String'
s = "hello Shubham"
s1 = "H" + s[1:]                   # update first character
s2 = s.replace("Shubham", "ShubhamMohite")  # replace word
print(s1)
print(s2)

'Upper case , Lower Case'
s = "Hello Shubham"
print(s.upper())
print(s.lower())

'Concatenating String'
s1 = "Hello, how are you"
s2 = "Shubham"
print(s1 + " " + s2)

'Using format()'
s = "My name is {} and I am {} years old.".format("Shubham", 22)
print(s)
