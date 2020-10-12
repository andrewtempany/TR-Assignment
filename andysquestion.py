#!/usr/bin/env python

import sys

filepath = "testFile.csv"

inFile = open(filepath, "r")
lines = inFile.readlines()
compdict = {}

for line in lines[1:]:

    elems = line.split(",")

    if elems[0] not in compdict:
        compdict[elems[0]] = 0
        compdict[elems[0]] += float(elems[1])
        compdict[elems[0]] += float(elems[2])*-1
    else:
        compdict[elems[0]] += float(elems[1])
        compdict[elems[0]] += float(elems[2])*-1

compdict['Utes'] += compdict['Utes LLC']
compdict['Utes'] += compdict['LLC Utes']
compdict['Utes'] += compdict['Utes Limited Liability Corp']
compdict['Utes'] += compdict['Utes Co.']
del compdict['LLC Utes']
del compdict['Utes Limited Liability Corp']
del compdict['Utes Co.']
del compdict['Utes LLC']


# utesNames = ["Utes", "Utes LLC", "LLC Utes",
#              "Utes Limited Liability Corp", "Utes Co."]


print(compdict)
