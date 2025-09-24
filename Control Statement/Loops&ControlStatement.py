# -*- coding: utf-8 -*-
"""
Created on Wed Sep 24 11:01:09 2025

@author: shubh
"""
'for loop'
# Iterating over a list
a = [1, 2, 3]
for i in a:
    print(i)
    
li = ["Python", "for", "loop"]
for index in range(len(li)):
    print(li[index])
else:
    print("Inside Else Block")

    
'While loop'    
# Using while loop
cnt = 0
while cnt < 5:
    print(cnt)
    cnt += 1    
    
cnt = 0
while (cnt < 3):
    cnt = cnt + 1
    print("While Loop")    
    

for i in range(1, 5):
    for j in range(i):
        print(i, end=' ')
    print()
    
 #Control Statement 
"Break"
# Using break to exit the loop
for i in range(10):
    if i == 5:
        break
    print(i)
    
'continue Statement'
# Using continue to skip an iteration
for i in range(10):
    if i % 2 == 0:
        continue
    print(i)

'pass Statement'
# Using pass as a placeholder
for i in range(5):
    if i == 3:
        pass  
    print(i)    