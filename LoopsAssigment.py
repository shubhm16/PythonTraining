#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 10 09:58:07 2024

@author: shubhammohite
"""
#1. Write a while loop to print the numbers from 1 to 10. Stop the loop if the
#number is equal to 7. 

'''number = 1
while (number<=7):
    print(number)
    number+=1'''
    
    
#2.Use a for loop to iterate over the list [2, 5, 8, 11, 14, 17, 20]. Add 3 to each
#element and store the updated values in a new list using list comprehension. 

'''list = [2, 5, 8, 11, 14, 17, 20]
new_list =[]
 
for i in list:
    new_list.append(i+3)

print(list,new_list,end="")'''

# Write a while loop that keeps asking the user to enter a positive number. If the
#user enters a negative number, stop the loop and print "Goodbye!". 
   
'''ask_number=int(input("enter only positive number"))

while ask_number>=0:
    ask_number=int(input("enter only positive number:"))
else:
    print("Goodbye!")'''
    
    
#Write a for loop that iterates through a list of integers [3, 5, 8, 12, 15]. Use a
#break statement to stop the iteration when the element is greater than 10, and
#print each number before the break. 

'''list=[3, 5, 8, 12, 15]
for i in list: 
    print(i)
    if i>=10:
        break'''
        
#Use a lambda function to create an anonymous function that takes a number
#and returns its square. Use it on a list of numbers [2, 3, 4, 5, 6] and display
#the result. 

'''square_function = lambda x: x ** 2
numbers = [2, 3, 4, 5, 6]
for i in range(len(numbers)):
    numbers[i] = square_function(numbers[i])

print(numbers)'''

#Write a for loop that uses a lambda function to filter out only even numbers
#from the list [1, 2, 3, 4, 5, 6, 7, 8] and print them. 

'''numbers = [1, 2, 3, 4, 5, 6, 7, 8]
even_numbers = filter(lambda x: x % 2 == 0, numbers)

for num in even_numbers:
    print(num)'''
    
    
#Create a lambda function that takes a string and returns it in reverse. Apply
#this function to the list of strings ["apple", "banana", "cherry"] and print the
#result.

'''
fruits = ["apple", "banana", "cherry"]
reverse_string = lambda x: x[::-1]
reversed_fruits = list(map(reverse_string, fruits))
print(reversed_fruits)'''

# 8. Write a user-defined function called is_prime(num) that takes a number as
# input and returns True if it is a prime number, otherwise returns False. Test it
# on numbers from 1 to 20 using a for loop.

'''
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True
for n in range(1, 21):
    print(f"{n} is prime: {is_prime(n)}")
'''

# 9. Write a user-defined function called is_palindrome(word) that checks if a word
# is a palindrome. Use a for loop and a lambda function to filter only the
# palindromes from the list ["radar", "hello", "level", "world", "rotor"].

'''
def is_palindrome(word):
    return word==word[::-1]
words=["radar", "hello", "level", "world", "rotor"]
palindrome=list(filter(lambda word:is_palindrome(word),words))
print(palindrome)'''


#10. With reference to snapshot, dataset name = data_assigns.csv attached in group.
#Please apply type casting and Imputation process with different strategy
#available on given dataset. Also provide its reason for the same. 

'''import pandas as pd

data_set = pd.read_csv(r'/Users/akashmohite/Downloads/Eda_Dataset/data_assigns.csv')
        
#type casting               
data_set.dtypes

data_set.head(10)
#to check Nan or null value
data_set.isnull()
data_set.isnull().sum()
data_set.notnull()
data_set.notnull().sum()

#change data type 
data_set.Age=data_set.Age.astype('int')


Top5Salary = data_set.nlargest(5, "Income") 
Top5YoungPerson= data_set.nsmallest(5,"Age")

#Replace NaN value with mean value
data_set['Age'].fillna(data_set['Age'].median(),inplace=True)
data_set
'''


import pandas as pd
education = pd.read_csv(r'')



















