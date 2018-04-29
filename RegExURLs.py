# -*- coding: utf-8 -*-
"""
Created on Mon Apr 23 00:33:58 2018
To capture information from groups()
@author: dongrp2
"""

import re

urls = '''
https://www.google.com
http://coreyms.com
https://youtube.com
https://www.nasa.gov
'''

pattern = re.compile(r'https?://(www\.)?(\w+)(\.\w+)')

matches = pattern.finditer(urls)
for match in matches:
    print(match.group(0)) # 0 entire URL 1 WWW 2 Domain
    
   
subbed_urls = pattern.sub(r'\2\3', urls)
print(subbed_urls)

# matches = pattern.finditer(urls)

# for match in matches:
#     print(match.group(3))

