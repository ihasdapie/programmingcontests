#!/usr/bin/python
#j1
import sys

inp = []
for line in sys.stdin:
	inp.append(int(line))
	
a = ((inp[0])*3)+((inp[1])*2)+inp[2]
b = ((inp[3])*3)+((inp[4])*2)+inp[5]

if a > b:
	print "A"
	
if a == b:
	print "T"

if b > a:
	print 'B'
