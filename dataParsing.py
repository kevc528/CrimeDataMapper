#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov  9 19:16:29 2019

@author: Kevin
"""

#data processing

#fObj = open("unprocessed.csv", 'r')
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
#
##adding city to addresses
#
#fObj = open('processedData1.csv', 'r')
#
#
#fObj2 = open('processedDataCities.csv' ,'w')
#
#for line in fObj:
#    lineCon = (line.strip().split(','))
#    lineCon[2] += " Philadelphia"
#    fObj2.write(lineCon[0] + ',' + lineCon[1] + ',' + lineCon[2] + ',' + lineCon[3] + '\n')
#    
#fObj2.close()
#
#
#
##sorting to lat long
#
#fileName = "processedDataCities1.csv"
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
#
#fileName = "processedDataCities1.csv"
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
#
##sorting categories
#
##theft, assault, sex crimes, fraud, other
#
#from nltk.corpus import wordnet
#
#theftSyn = []
#assaultSyn = []
#sexSyn = []
#fraudSyn = []
#
#def appendToList (lName, word):
#    for syn in wordnet.synsets(word):
#        for l in syn.lemmas():
#            if '_' in l.name():
#                new = l.name().replace('_',' ')
#                lName.append(new)
#            else:
#                lName.append(l.name())
#
#appendToList(theftSyn, "theft")
#appendToList(theftSyn, "steal")
#theftSyn.append("remove")
#theftSyn.append("taken")
#theftSyn.append("grabbed")
#theftSyn.append("snatch")
#theftSyn.append("money")
#theftSyn.append("stolen")
#theftSyn.append("property")
#theftSyn.append("robbery")
#
#
#
#appendToList(assaultSyn, "assault")
#appendToList(assaultSyn, "hit")
#appendToList(assaultSyn, "punch")
#appendToList(assaultSyn, "attack")
#assaultSyn.remove("rape")
#assaultSyn.remove("make")
#assaultSyn.remove("off")
#assaultSyn.remove("gain")
#assaultSyn.remove("rape")
#assaultSyn.remove("round")
#assaultSyn.remove("round")
#assaultSyn.remove("attempt")
#assaultSyn.remove("violation")
#assaultSyn.remove("violate")
#assaultSyn.remove("fire")
#assaultSyn.append("slap")
#assaultSyn.append("struck")
#
#
#appendToList(sexSyn, "touch")
#appendToList(sexSyn, "rape")
#appendToList(sexSyn, "indecent")
#sexSyn.remove("hint")
#sexSyn.remove("spot")
#sexSyn.remove("stir")
#sexSyn.remove("refer")
#sexSyn.remove("pertain")
#sexSyn.remove("relate")
#sexSyn.remove("come to")
#sexSyn.remove("violation")
#sexSyn.remove("meet")
#sexSyn.remove("affect")
#sexSyn.remove("match")
#sexSyn.remove("equal")
#sexSyn.append("inappropriate")
#sexSyn.append("sex")
#
#
#fObj = open("lat_long.csv", "r")
#
#fObj2 = open("processedDataCities.csv", "r")
#
#def sortSentence(text):
#    for syn in theftSyn:
#        if syn in text:
#            return "theft"
#    for syn in sexSyn:
#        if syn in text:
#            return "sex"
#    for syn in assaultSyn:
#        if syn in text:
#            return "assault"
#    return "other"
#        
#fObjW = open("final_crime_sorted.csv", "w")
#
#for line in fObj:
#    contents = line.strip().split(",")
#    lat_long = contents[:2]
#    fObj2Line = fObj2.readline()
#    fObjW.write(lat_long[0]+","+lat_long[1]+","+fObj2Line.strip()+","+sortSentence(fObj2Line.lower())+'\n')
#
#fObj.close()
#fObjW.close()
#
#fObj = open("final_crime_sorted1.csv")
#
#fObj2 = open("sorted_with_24hr_time.csv", "w")
#
#for line in fObj:
#    contents = line.strip().split(",")
#    timing = contents[3].strip().replace(".", "").replace(" ", "").upper();
#    if timing[-2:] == "PM":
#        if len(timing) > 6 :
#            hour = int(timing[:2])
#            if timing[:2] != "12":
#                hour = int(timing[:2]) + 12
#            minute= timing[3:5]
#            timing = str(hour) + ":" + minute
#        else:
#            hour = int(timing[:1]) + 12
#            minute = timing[2:4]
#            timing = str(hour) + ":" + minute
#    if timing[-2:] == "AM":
#        if len(timing) > 6:
#            hour = timing[:2]
#            minute = timing[3:5]
#            if hour == "12":
#                hour = "00"
#            timing = hour + ":" + minute
#        else:
#            hour = "0" + timing[0]
#            minute = timing[2:4]
#            timing = hour + ":" + minute
#    contents[3] = timing
#    fObj2.write(contents[0]+","+contents[1]+","+contents[2]+","+contents[3]+","+contents[4]+","+contents[5]+","+contents[6]+"\n")
#
#fObj2.close()
#fObj.close()

# mapping occurence of hour

timeMap = {}
dateMap = {}
theftTimeMap = {}
assaultTimeMap = {}
sexTimeMap = {}

fObj = open("sorted_with_24hr_time.csv")

for line in fObj:
    contents = line.strip().split(",")
    date = int(contents[2].split("/")[1])
    time = contents[3][:2]
    if time in timeMap:
        timeMap[time] += 1
    else:
        timeMap[time] = 1
    if date in dateMap:
        dateMap[date] += 1
    else:
        dateMap[date] = 1
    if contents[6] == 'theft':
        if time in theftTimeMap:
            theftTimeMap[time] += 1
        else:
            theftTimeMap[time] = 1
    if contents[6] == 'assault':
        if time in assaultTimeMap:
            assaultTimeMap[time] += 1
        else:
            assaultTimeMap[time] = 1    
    if contents[6] == 'sex':
        if time in sexTimeMap:
            sexTimeMap[time] += 1
        else:
            sexTimeMap[time] = 1
            
timeKeys = []
timeVals = []

for keys in timeMap:
    timeKeys.append(int(keys))
    timeVals.append(int(timeMap[keys]))
    
dateKeys = []
dateVals = []

for keys in dateMap:
    dateKeys.append(int(keys))
    dateVals.append(int(dateMap[keys]))

theftKeys = []
theftVals = []

for keys in theftTimeMap:
    theftKeys.append(int(keys))
    theftVals.append(int(theftTimeMap[keys]))
    
assaultKeys = []
assaultVals = []

for keys in assaultTimeMap:
    assaultKeys.append(int(keys))
    assaultVals.append(int(assaultTimeMap[keys]))

sexKeys = []
sexVals = []

for keys in sexTimeMap:
    sexKeys.append(int(keys))
    sexVals.append(int(sexTimeMap[keys]))
        
from matplotlib import pyplot as plt

#plt.bar(timeKeys, timeVals)
#plt.ylabel('Number of Crimes')
#plt.xlabel('Hour of Day')
#plt.title('Crimes by Hour')
#plt.show()
#
#plt.bar(dateKeys, dateVals)
#plt.ylabel('Number of Crimes')
#plt.xlabel('Day of Month')
#plt.title('Crimes by Day of Month')
#plt.show()

plt.bar(theftKeys, theftVals)
plt.ylabel('Number of Thefts')
plt.xlabel('Hour of Day')
plt.title('Thefts by Hour')
plt.show()

plt.bar(assaultKeys, assaultVals)
plt.ylabel('Number of Assaults')
plt.xlabel('Hour of Day')
plt.title('Assaults by Hour')
plt.show()

plt.bar(sexKeys, sexVals)
plt.ylabel('Number of Sex Crimes')
plt.xlabel('Hour of Day')
plt.title('Sex Crimes by Hour')
plt.show()


