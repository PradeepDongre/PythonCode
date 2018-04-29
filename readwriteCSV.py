# -*- coding: utf-8 -*-
"""
Created on Sun Apr 22 14:23:32 2018
CSV module handles parsing better as delimiter can be part of data as well
@author: dongrp2
"""
import csv

with open('names.csv','r') as names_csv:
    csv_reader = csv.reader(names_csv)
    next(csv_reader) # to loop over the first line which is headder
    for line in csv_reader:
        #print(line) #print all the lines in list
        print(line[2]) # 2nd index of the list
        
"""Creating a tab delimited file"""
        
with open('names.csv','r') as names_csv:
    csv_reader = csv.reader(names_csv)
      
    with open('new_names.csv','w') as new_names:
        csv_writer = csv.writer(new_names, delimiter='\t')
        
        for line in csv_reader:
            csv_writer.writerow(line)
 
#    with open('new_names.csv','r') as read_new_csv:
#        csv_new_reader =  csv.reader(read_new_csv,delimiter='\t')
#        for line in csv_new_reader:
#            print(line)
    
"""Using Dictionary Reader where field names are keys of the values"""
with open('names.csv','r') as names_csv:
    csv_reader = csv.DictReader(names_csv)    
    
    for line in csv_reader:
        print(line['email']) #accesing the key 'email'
        
"""Using Dictionary Writer have to provide the field names"""
with open('names.csv','r') as names_csv:
    csv_reader = csv.DictReader(names_csv)   
    
    with open('new_names_dict.csv','w') as new_names_dict:
         fieldnames = ['first_name','last_name','email']
         csv_writer = csv.DictWriter(new_names_dict, fieldnames=fieldnames, delimiter='\t')
         csv_writer.writeheader()
    
         for line in csv_reader:
             #del line['email'] if want to write only first and last name
             csv_writer.writerow(line)
    #for line in csv_reader:
     #   print(line['email']) #accesing the key 'email'        

        
        
        
        