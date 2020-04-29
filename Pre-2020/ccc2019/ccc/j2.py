#!/usr/bin/python
#j2
import sys
inp = []
for line in sys.stdin:
	inp.append(line.rstrip())

inp = inp[1:]

inp = map(lambda x: x.split(' '), inp)
inp = map(lambda x: (int(x[0]),x[1]), inp)

out = []

for x in inp:
	temp = ""
	for y in range(x[0]):
		temp = temp + x[1]
	out.append(temp)
for x in out:
	print x

