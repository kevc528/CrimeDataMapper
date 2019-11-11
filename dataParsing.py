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

#theft, assault, sex crimes, fraud, other

from nltk.corpus import wordnet

theftSyn = []
assaultSyn = []
sexSyn = []
fraudSyn = []

def appendToList (lName, word):
    for syn in wordnet.synsets(word):
        for l in syn.lemmas():
            if '_' in l.name():
                new = l.name().replace('_',' ')
                lName.append(new)
            else:
                lName.append(l.name())

appendToList(theftSyn, "theft")
appendToList(theftSyn, "steal")
theftSyn.append("remove")
theftSyn.append("taken")
theftSyn.append("grabbed")
theftSyn.append("snatch")
theftSyn.append("money")
theftSyn.append("stolen")
theftSyn.append("property")
theftSyn.append("robbery")



appendToList(assaultSyn, "assault")
appendToList(assaultSyn, "hit")
appendToList(assaultSyn, "punch")
appendToList(assaultSyn, "attack")
assaultSyn.remove("rape")
assaultSyn.remove("make")
assaultSyn.remove("off")
assaultSyn.remove("gain")
assaultSyn.remove("rape")
assaultSyn.remove("round")
assaultSyn.remove("round")
assaultSyn.remove("attempt")
assaultSyn.remove("violation")
assaultSyn.remove("violate")
assaultSyn.remove("fire")
assaultSyn.append("slap")
assaultSyn.append("struck")


appendToList(sexSyn, "touch")
appendToList(sexSyn, "rape")
sexSyn.remove("hint")
sexSyn.remove("spot")
sexSyn.remove("stir")
sexSyn.remove("refer")
sexSyn.remove("pertain")
sexSyn.remove("relate")
sexSyn.remove("come to")
sexSyn.remove("violation")
sexSyn.remove("meet")
sexSyn.remove("affect")
sexSyn.remove("match")
sexSyn.remove("equal")
sexSyn.append("inappropriate")
sexSyn.append("sex")


fObj = open("lat_long.csv", "r")

fObj2 = open("processedDataCities.csv", "r")

def sortSentence(text):
    for syn in theftSyn:
        if syn in text:
            return "theft"
    for syn in assaultSyn:
        if syn in text:
            return "assault"
    for syn in sexSyn:
        if syn in text:
            return "sex"
    return "other"
        
fObjW = open("final_crime_sorted.csv", "w")

for line in fObj:
    contents = line.strip().split(",")
    lat_long = contents[:2]
    fObj2Line = fObj2.readline()
    fObjW.write(lat_long[0]+","+lat_long[1]+","+fObj2Line.strip()+","+sortSentence(fObj2Line.lower())+'\n')


fObjW.close()