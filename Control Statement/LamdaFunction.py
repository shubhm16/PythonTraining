# -*- coding: utf-8 -*-
"""
Created on Wed Sep 24 12:31:08 2025

@author: shubh
"""

s1 = 'practicemakemanperfect'
s2 = lambda func: func.upper()
print(s2(s1))



'Condition Checking'

n = lambda x: "Positive" if x > 0 else "Negative" if x < 0 else "Zero"
print(n(5))   
print(n(-3))  
print(n(0))

check = lambda x: "Even" if x % 2 == 0 else "Odd"
print(check(4))  
print(check(7))