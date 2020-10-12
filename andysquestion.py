#!/usr/bin/env python

import sys

filepath = "Desktop/testfile.txt"

inFile = open(filepath, "r")
compdict = {}

for line in inFile:
	elems = line.split(",")
	if elems[0] not in compdict:
		compdict[elems[0]] = 0
		compdict[elems[0]] += float(elems[1])
		compdict[elems[0]] += float(elems[2])*-1
	else:
		compdict[elems[0]] += float(elems[1])
		compdict[elems[0]] += float(elems[2])*-1

compdict['calvin'] += compdict['cal']
compdict['calvin'] += compdict['charlie']
del compdict['cal']
del compdict['charlie']

print(compdict)
