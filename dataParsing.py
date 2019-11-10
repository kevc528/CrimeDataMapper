#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov  9 19:16:29 2019

@author: Kevin
"""

#data processing

#fileName = input("Input a file name: ")
#
#fObj = open(fileName, 'r')
#
#contents = []
#
#for line in fObj:
#    if len(line) > 1:
#        contents.append(line.strip().split(". "))
#    
#fObj2 = open('processedData', 'w')
#    
#for post in contents:
#    counter = 0
#    for item in post:
#        if counter <= 3:
#            fObj2.write(item + ",")
#            counter += 1
#        else:
#            fObj2.write(item)
#    fObj2.write('\n')
#    
#fObj2.close()

#adding city to addresses

#fObj = open('processedData1.csv', 'r')
#
#
#fObj2 = open('processedDataCities1.csv' ,'w')
#
#for line in fObj:
#    lineCon = (line.strip().split(','))
#    lineCon[2] += " Philadelphia"
#    fObj2.write(lineCon[0] + ',' + lineCon[1] + ',' + lineCon[2] + ',' + lineCon[3] + '\n')
#    
#fObj2.close()



#sorting to lat long

#fileName = input("Input a file name: ")
#
#fObj = open(fileName, 'r')
#
#fObj2 = open('addresses.csv', 'w')
#
#for line in fObj:
#    lineCon = line.strip().split(',')
#    fObj2.write(lineCon[2] + '\n')
#
#fObj2.close()

fileName = input("Input a file name: ")

fObj = open(fileName, 'r')

fObj2 = open('addresses.csv', 'w')

for line in fObj:
    lineCon = line.strip().split(',')
    fObj2.write(lineCon[2] + '\n')

fObj2.close()