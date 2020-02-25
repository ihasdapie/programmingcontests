#!/usr/bin/python
#j5

from itertools import permutations
from itertools import combinations_with_replacement

import sys
inp = []
for ayy in sys.stdin:
	inp.append(ayy.rstrip('\n'))
	
print inp

r1 = tuple(inp[0].split(' '))
r2 = tuple(inp[1].split(' '))
r3 = tuple(inp[2].split(' '))

targets = tuple(inp[3].split(' '))
print r1, r2, r3
steps = targets[0]
initialAHH = targets[1]
final = targets[2]

possible_method = []
for x in combinations_with_replacement(range(3),int(steps)):
	possible_method.append(x)

possible_methods = []

for x in possible_method:
	for y in permutations(x):
		possible_methods.append(y)

solutions = []
print possible_methods
for x in possible_methods:
	initial = initialAHH[:]

	for y in x:
		if y == 0:
			initial = initial.replace(str(r1[0]),str(r1[1]))
		if y == 1:
			initial = initial.replace(str(r2[0]),str(r2[1]))
		if y == 2:
			initial = initial.replace(str(r3[0]),str(r3[1]))
		print initial, y
	if initial == final:
		solutions.append(x)
		
print solutions[-1]
