# -*- coding: utf-8 -*-
"""
Created on Sun Apr 29 12:05:41 2018

@author: dongrp2
"""
#if else
print ("Enter a number: ")
num = int(input())
n = num % 2 

if n == 0 and (2<= num <=5): 
    print('Not Weird')
elif n == 0 and (6<= num <=20): 
    print('Weird')
elif n == 0 and num > 20: 
    print("Not Weird")
elif num % 2 != 0: 
    print('Weird')
    
#Arithmatic operator
    print ("Enter number a: ")
    a = int(input())
    print ("Enter number b: ")
    b = int(input())

    print("a+b = %d\na-b = %d\na*b = %d"%(a+b,a-b,a*b))
    
#Division
    print ("Enter number a: ")
    a = int(input())
    print ("Enter number b: ")
    b = int(input())
    x = int(a/b)
print(x)
print (a/b)

#loops
print ("Enter number n: ")   
n = int(input())
for i in range(n): 
    print("i=\n"%i**2,end='')

    
counter = 0;
while  counter < n :
        print (counter**2)
        counter = counter + 1    

print ("Enter number n: ")   
n = int(input())
for x in range(1,n+1):
    print(x,end='')

# Generator
def square_numbers(nums):
    result = []
    for i in nums:
        result.append(i*i)
    return result

my_nums = square_numbers([1,2,3,4,5])
print (my_nums) #[1, 4, 9, 16, 25]

#Use "yeild" keyword to convert it to Generator
def square_numbers(nums):
    for i in nums:
        yield (i*i)
my_nums = square_numbers([1,2,3,4,5])
for num in my_nums:
    print (num)     
        
#list comprehension
my_nums = [x*x for x in [1,2,3,4,5]]
for nums in my_nums:
    print (nums)

#Converting to generator  
my_nums = (x*x for x in [1,2,3,4,5])
print (my_nums)
#print list(my_nums)
for nums in my_nums:
    print (nums)
    
#Python Interview
#1 Whiteboarding
#2 Control flow for while if else
    for i in range(1,11):
        print (i)
        
i = 1
while i <= 10:
    print (i)
    i += 1 
    
a = 10
b = 20
if a < b:
    print ("{} ia less than {}".format(a,b))
elif a == 20:
    print ("{} ia equal to {}".format(a,b))
else:
    print ("{} ia greater than {}".format(a,b))
    
#3 How you used in Python cool programm you have written
    
import os, glob
os.chdir ("C:/users/dongrp2")
for file in glob.glob("*.jpg"):
    print(file)
    
#4 Fizz Buzz if divisible by 3 Fizz if by 5 Buzz by both FizzBuzz
for num in range(1,100):
    if num % 5 == 0 and num % 3 == 0:
        print("FizzBuzz")
    elif num % 3 ==0:
        print ("Fizz")
    elif num % 5 ==0:
        print ("Buzz")
    else:
        print (num)
#Fibonacci Sequence number is a sum of previous two numbers
a,b = 0,1  #assignment
for i in range (0,10):
 print(a)
 a,b = b, a + b    
 
#5 Basic Data Types
#Lists Homogeneous collection
 my_list = [10,20,30,40,50]
 for i in my_list:
     print (i)
#Tuples Hetrogenous collection
 my_tup = (1,2,3,4,5)
 for i in my_tup:
     print (i)
#Dict Hash table
my_dict = {'name': 'PK', 'age':'5', 'occupation':'Consultant'}
for key,val in my_dict.iteritems():
    print ("My {} is {}".format(key,val))
#set
my_set = {10,20,30,40,50,60,50,30}
for i in my_set:
    print(i)
    
#6 List comprehenssions
my_list = [10,20,30,40,50]
squares = [num*num for num in my_list]
print (squares)

#7 Generators
def fib(num):
    a,b = 0,1
    for i in range(0,num):
        yield "{}: {}".format(i+1,a)
        a,b = b, a + b
for item in fib(10):
    print (item)
    
#8 OOP
class Person(object): #inherit from object
    def __inti__(self, name):
        self.name = name #initialize
        
    def revel_identity(self):
        print ("My name is {}".format(self.name))
        
class SuperHero(Person): #Inherit class Person
    def __inti__(self, name, hero_name): #Initialize ofF of base class
        super(SuperHero, self).__init__(name)
        self.hero_name = hero_name
        
    def revel_identity(self): #Override Method
        super(SuperHero, self).revel_identity()
        print ("...And I am {}".format(self.hero_name))
        
PK = Person('PK') #instance of class Person
PK.revel_identity()

Golu = SuperHero('PK','Golu')
Golu.revel_identity
	