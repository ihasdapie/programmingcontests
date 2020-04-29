import sys
from itertools import combinations

sys.setrecursionlimit(1000000)
numString = int(input())

strList= []
for i in range(numString):
	strList.append(input())


def findSubString(string):
	global currentSubStringSet

	for x in range(len(string)):
		for y in range(len(string)-x):
			currentSubStringSet.add(string[x:x+y+1])


#solution with recursion
#~ currentSubStringSet = {""}

#~ for i in strList:
	#~ findSubString(i)
	#~ print(len(currentSubStringSet))

	#~ currentSubStringSet = {""}

#alternate solution with list comprehension

for s in strList:
	print(len(set(tuple(s[i:i+j+1] for i in range(len(s)) for j in range(len(s)-i))))+1)

#alternate solution with itertools
	
for s in strList:
	print(len(set(tuple(s[i:j] for i,j in combinations(range(len(s)+1), r = 2))))+1)
	#~ print(set(tuple(s[i:j] for i,j in combinations(range(len(s)), r = 2))))

for k in range(int(input())):
    s = input()
    print(len(set(tuple(s[i:i+j+1] for i in range(len(s)) for j in range(len(s)-i))))+1)


