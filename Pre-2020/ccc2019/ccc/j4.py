#!/usr/bin/python
#j4

import sys
line = ''
for ayy in sys.stdin:
	line = line + ayy
	
H = line.count('H')
V = line.count('V')


flippygrid = [[1,2],[3,4]]

def flipv(x):
	x[0],x[1] = x[1],x[0]
	return x

def fliph(x):
	a = x[0][0]
	b = x[0][1]
	c = x[1][0]
	d = x[1][1]
	return [[b,a],[d,c]]

if H % 2 == 1:
	flippygrid = fliph(flippygrid)

if V % 2 == 1:
	flippygrid = flipv(flippygrid)

#OUTPUT:
print flippygrid[0][0]," ", flippygrid[0][1]
print flippygrid[1][0]," ", flippygrid[1][1]
