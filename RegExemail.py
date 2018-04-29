# -*- coding: utf-8 -*-
"""
Created on Mon Apr 23 00:22:40 2018

@author: dongrp2
"""

import re

emails = '''
CoreyMSchafer@gmail.com
corey.schafer@university.edu
corey-321-schafer@my-work.net
'''

pattern = re.compile(r'[a-zA-Z]+@[a-zA-Z]+\.com') #1st
pattern = re.compile(r'[a-zA-Z.]+@[a-zA-Z]+\.(com|edu)') #2nd
pattern = re.compile(r'[a-zA-Z0-9.-]+@[a-zA-Z-]+\.(com|edu|net)') #2nd
pattern = re.compile(r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+')

matches = pattern.finditer(emails)

for match in matches:
    print(match)