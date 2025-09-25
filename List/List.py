# -*- coding: utf-8 -*-
"""
Created on Wed Sep 24 11:34:18 2025

@author: shubh
"""
'Square brackets'
a = [100, 22, 300, 4234, 5555] # List of integers
b = ['apple', 'banana', 'cherry'] # List of strings
c = [1, 'hello', 3.14, True] # Mixed data types

print(a)
print(b)
print(c)


'list() '
a = list((1, 2, 3, 'apple', 4.5))  
print(a)

b = list("RAM")
print(b)

'Replacement elements'

a = [2] * 6
b = [0] * 8

print(a)
print(b)

'List Accessing'
a = [101, 20, 230, 840, 50]
print(a[0])    
print(a[-1])
print(a[1:4])   # elements from index 1 to 3


"Adding elements in List"

a = []

a.append(10)  
print("After append(10):", a)  

a.insert(0, 5)
print("After insert(0, 5):", a) 

a.extend([15, 20, 25])  
print("After extend([15, 20, 25]):", a) 

a.clear()
print("After clear():", a)


'Update'
a = [10, 20, 30, 40, 50]
a[1] = 25 
print(a)

'Remove elements from list'
a = [10, 20, 30, 40, 50]

a.remove(30)  
print("After remove(30):", a)

popped_val = a.pop(1)  
print("Popped element:", popped_val)
print("After pop(1):", a) 

del a[0]  
print("After del a[0]:", a)

