# -*- coding: utf-8 -*-
"""
Created on Sun Apr 22 09:22:37 2018
test.txt and the FileOperations both are in same directory
r read
w write
a append
r+ read write
@author: dongrp2
"""
"""
f = open('test.txt','r') 

print(f.name)
print(f.mode)

f.close()
"""
"""Conext Manager(with keyword) better way so that explicit close is not require/"""

with open('test.txt','r') as f:
    print(f.name)
    print(f.mode)
    
"""f is file object variable and can be accessed outside context"""
with open('test.txt','r') as f:
    pass
print(f.closed)
#print(f.read()) #result in I/O error as file closed

with open('test.txt','r') as f:
    f_contents = f.read()
    print(f_contents)
    
"""reads all contents as a list readlines()"""    
with open('test.txt','r') as f:
    f_contents_list = f.readlines()
    print(f_contents_list)
    
"""reads first line readline(), end='' to remove new lines"""    
with open('test.txt','r') as f:
    f_contents_list = f.readline()
    print(f_contents_list, end='')
    
    f_contents_list = f.readline()
    print(f_contents_list, end='')
    
    
""" print file using  for efficient as it is not reading all contents at once. One line at a time"""
with open('test.txt','r') as f:
    for line in f:
        print(line,end='')

"""reading by size read(No of Characters to read)"""
with open('test.txt','r') as f:
    
    f_contents = f.read(100)
    print(f_contents,end='') ##100
    
    f_contents = f.read(100)
    print(f_contents,end='') #next 100 characters
    
"""Read 100 characters with while loop """
with open('test.txt','r') as f:
     size_to_read = 100
     f_contents = f.read(size_to_read)
     
     while len(f_contents) > 0:
         print(f_contents,end='')
         f_contents = f.read(size_to_read)
    
"""Read 10 characters with while loop and * at end of every 10 characters and tell() to get the position"""
with open('test.txt','r') as f:
     size_to_read = 10
     f_contents = f.read(size_to_read)
     
     while len(f_contents) > 0:
         print(f_contents,end='*')
         print(f.tell())
         f_contents = f.read(size_to_read)   
         
"""Read 10 characters with while loop and * at end of every 10 characters and tell() to get the position"""
with open('test.txt','r') as f:
     size_to_read = 10
     f_contents = f.read(size_to_read)
     print(f_contents,end='*')
     f.seek(0)
     f_contents = f.read(size_to_read)
     print(f_contents,f.tell())
    
"""write to a read mode file UnsupportedOperation: not writable"""
with open('test.txt','r') as f:
    f.write('PK TEST')
    
"""To create empty non existent file"""
with open('test2.txt','w') as f:
     pass
 
"""Write seek () to put some thing at 1st character"""
with open('test2.txt','w') as f:
    f.write('Test')
    f.seek(0)
    f.write('Ri')
    
"""to create copy of a file"""
with open('test.txt','r') as rf:
    with open('test_copy.txt','w') as wf:
        for line in rf:
            wf.write(line)
    
    
"""to create copy of a file"""
with open('AWS.PNG','rb') as rf:
    with open('AWS_copy.PNG','wb') as wf:
        for line in rf:
            wf.write(line)
    
"""to create copy of a file"""
with open('AWS.PNG','rb') as rf:
    with open('AWS_copy.PNG','wb') as wf:
     chunk_size = 4096
     rf_chunk = rf.read(chunk_size)
     while len(rf_chunk) > 0:
        wf.write(rf_chunk)
        rf_chunk = rf.read(chunk_size)  
    
    
    
    
    
    
    
    
    
    
    
    
    