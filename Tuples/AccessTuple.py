# -*- coding: utf-8 -*-
"""
Created on Wed Sep 24 11:49:07 2025

@author: shubh
"""

# Accessing Tuple with Indexing
tup = tuple("Geeks")
print(tup[0])

# Accessing a range of elements using slicing
print(tup[1:4])  
print(tup[:3])

# Tuple unpacking
tup = ("Geeks", "For", "Geeks")

# This line unpack values of Tuple1
a, b, c = tup
print(a)
print(b)
print(c)


'Concatenation of Tuples'
tup1 = (0, 1, 2, 3)
tup2 = ('Have', 'a', 'nice','day')

tup3 = tup1 + tup2
print(tup3)


'Slicing of Tuple'

tup = tuple('INDIAISNOTFORPROPEOPLE')

# Removing First element
print(tup[1:])

# Reversing the Tuple
print(tup[::-1])

# Printing elements of a Range
print(tup[4:9])


'delete tuple'

tup = (0, 1, 2, 3, 4)
del tup

print(tup) //tuples are immutable, we cannot delete individual elements 