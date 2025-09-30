# -*- coding: utf-8 -*-
"""
Created on Wed Sep 24 12:06:10 2025

@author: shubh
"""

set1 = set()
print(set1)

set1 = set("GHraisoni college")
print(set1)

# Creating a Set with the use of a List
set1 = set(["G", "H", "Raisoni"])
print(set1)

# Creating a Set with the use of a tuple
tup = ("College", "for", "Nagpur")
print(set(tup))

# Creating a Set with the use of a dictionary
d = {"Nagpur": 1, "for": 2, "City": 3}
print(set(d))

'adding elemnts in sets'
# Creating a set
set1 = {1, 2, 3}

# Add one item
set1.add(4)

# Add multiple items
set1.update([5, 6])

print(set1)

'Accessing a Set'

set1 = set(["Man", "For", "Reasons."])

# Accessing element using For loop
for i in set1:
    print(i, end=" ")

# Checking the element# using in keyword
print("Geeks" in set1)

'Remove method'
# Using Remove Method
set1 = {1, 2, 3, 4, 5}
set1.remove(3)
print(set1)  

# Attempting to remove an element that does not exist
try:
    set1.remove(10)
except KeyError as e:
    print("Error:", e)  

# Using discard() Method
set1.discard(4)
print(set1)  

# Attempting to discard an element that does not exist
set1.discard(10)  # No error raised
print(set1)