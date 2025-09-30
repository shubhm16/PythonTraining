# -*- coding: utf-8 -*-
"""
Created on Wed Sep 24 11:46:42 2025

@author: shubh
"""

tup = ()
print(tup)

# Using String
tup = ('Shubham', 'For')
print(tup)

# Using List
li = [1, 2, 4, 5, 6]
print(tuple(li))

# Using Built-in Function
tup = tuple('Training')
print(tup)


'mixed data type tuples'
tup = (5, 'Welcome', 7, 'Shubham')
print(tup)

# Creating a Tuple with nested tuples
tup1 = (0, 1, 2, 3)
tup2 = ('python', 'Training')
tup3 = (tup1, tup2)
print(tup3)

# Creating a Tuple with repetition
tup1 = ('Java',) * 3
print(tup1)

# Creating a Tuple with the use of loop
tup = ('Ram')
n = 5
for i in range(int(n)):
    tup = (tup,)
    print(tup)