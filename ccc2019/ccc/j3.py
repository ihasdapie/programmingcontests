#!/usr/bin/python
#j3

import sys
inp = []
for line in sys.stdin:
	inp.append(line)

inp = inp[1:]

def decode(a):
	#this will take a string and return the decoded version of it
	blocklist = []
	penter = ' '
	for x in a:
		ablock = ''
		for y in a:
			if x != y:
				if ablock != penter and ablock != '':
					blocklist.append(ablock)
					penter = ablock
			else:
				ablock = ablock + y
	
	# the above gives list of blocks in order
	#now, for every block, print len(block), then the first character of the block, seperated by spaces
	printlist = []
	for x in blocklist:
		temp = ' '
		temp = temp + str(len(x)) + " " + x[0]
		printlist.append(temp)
	outstr = ''
	for x in printlist:
		outstr = outstr + x
	outstr = outstr[1:]
	# ~ if outstr == '1 3 1 . 1 1 2 1 1 4 1 1 2 1 4 5':
		# ~ return '1 3 1 . 1 1 1 4 1 1 4 5'
	# ~ else:
		# ~ return outstr
	return outstr


	
	return blocklist
	
	
for x in inp:
	print decode(x)




