# -*- coding: utf-8 -*-
"""
Created on Sun Apr 22 20:12:15 2018
Regular Expression
@author: dongrp2
"""
import re

print('\tTab')   #   Tab
print(r'\tTab')  #\tTab

text_to_search = '''
abcdefghijklmnopqurtuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
1234567890
Ha HaHa
MetaCharacters (Need to be escaped):
. ^ $ * + ? { } [ ] \ | ( )
coreyms.com
pk_rjit
321-555-4321
123.555.1234
123*555*1234
800-555-1234
900-555-1234
Mr. Schafer
Mr Smith
Ms Davis
Mrs. Robinson
Mr. T
mat
pat
bat
'''

sentence = 'Start a sentence and then bring it to an end'
"""re.compile method to write expressions
allows to separate patterns to a variable"""

#pattern = re.compile(r'abc')
#pattern = re.compile(r'coreyms\.com')
#pattern = re.compile(r'.') #Everything but new line
#pattern = re.compile(r'\d') # 0 - 9
#pattern = re.compile(r'\D') #not a digit
#pattern = re.compile(r'\w') # a-z A-Z 0-9 _ Underscore
#pattern = re.compile(r'\W') #Not a Character
#pattern = re.compile(r'\s') #Space Tab Newline
#pattern = re.compile(r'\s') #Not a Space Tab New Line
#pattern = re.compile(r'\bHa') #1stHa and 2nd Ha 
#pattern = re.compile(r'\BHa') #3rd Ha
#matches = pattern.finditer(text_to_search)
 
pattern = re.compile(r'^start',re.IGNORECASE) #Start of the string
pattern = re.compile(r'end$') #Start of the string
matches = pattern.finditer(sentence)

for match in matches:
    print(match)
    #Phone Number Match
pattern = re.compile(r'\d\d\d.\d\d\d.\d\d\d\d')
pattern = re.compile(r'\d\d\d[-.]\d\d\d[-.]\d\d\d\d') #Matching within a Character set [-.] dash OR a DOT
pattern = re.compile(r'[89]00[-.]\d\d\d[-.]\d\d\d\d') # 800 OR 900 Number
pattern = re.compile(r'[1-5]') # range 1 to 5
pattern = re.compile(r'[^a-zA-Z]') #within a Character set [] ^ act as negation 
pattern = re.compile(r'[^b]at')
matches = pattern.finditer(text_to_search) 
for match in matches:
    print(match)
    
 # phone number match in a file
with open('data.txt','r') as f:
     contents = f.read() 
     
     matches = pattern.finditer(contents)
     
     for match in matches:
         print(match)
    
#print(text_to_search[1:4])   #abc

# dot . is a special character in RE
         
#Quantifier to match multiple charater at a time. They goes in behind
         
pattern = re.compile(r'Mr\.?\s[A-Z]\w*')
pattern = re.compile(r'M(r|s|rs)\.?\s[A-Z]\w*')
pattern = re.compile(r'\d{3}.\d{3}.\d{4}')
#matches = pattern.finditer(text_to_search) #Extra functionality of match object
matches = pattern.findall(text_to_search) 
for match in matches:
    print(match)