# -*- coding: utf-8 -*-
"""
Created on Wed Sep 24 11:41:23 2025

@author: shubh
"""

'Python array'
import array as arr
a = arr.array('i', [1, 2, 3])

# accessing First Araay
print(a[0])

# adding element to array
a.append(5)
print(a)

'Access array '
import array as arr
a = arr.array('i', [1, 2, 3, 4, 5, 6])

print(a[0])
print(a[3])

b = arr.array('d', [2.5, 3.2, 3.3])
print(b[1])
print(b[2])


'remove elements from array'

import array
a = array.array('i', [1, 2, 3, 1, 5])

# remove first occurance of 1
a.remove(1)
print(a)

# remove item at index 2
a.pop(2)
print(a)


'Search element in array'
import array
a = array.array('i', [1, 2, 3, 1, 2, 5])

# index of 1st occurrence of 2
print(a.index(2))

# index of 1st occurrence of 1
print(a.index(1))


'Update value in array'
import array
a = array.array('i', [1, 2, 3, 1, 2, 5])

# update item at index 2
a[2] = 6
print(a)

# update item at index 4
a[4] = 8
print(a)

'reverse value in array'
import array
a = array.array('i', [1, 2, 3, 4, 5])

a.reverse()
print(*a)

'Extend element in array'

import array as arr 
a = arr.array('i', [1, 2, 3,4,5])

a.extend([6,7,8,9,10])
print(a)