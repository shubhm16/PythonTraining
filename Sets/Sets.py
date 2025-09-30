# -*- coding: utf-8 -*-
"""
Created on Wed Sep 24 12:04:25 2025

@author: shubh
"""

'How to create set'
set1 = {1, 2, 3, 4}
print(set1)

"use of set "
set1 = set()
print(set1)

set1 = set("GeeksForGeeks")
print(set1)

# Creating a Set with the use of a List
set1 = set(["Geeks", "For", "Geeks"])
print(set1)

# Creating a Set with the use of a tuple
tup = ("Geeks", "for", "Geeks")
print(set(tup))

# Creating a Set with the use of a dictionary
d = {"Geeks": 1, "for": 2, "Geeks": 3}
print(set(d))