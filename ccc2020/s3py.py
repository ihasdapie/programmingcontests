from itertools import permutations

needle = input()
haystack = input()

uSub = {""}

if len(needle) > len(haystack):
	print(0)


else:
	poss = set([x for x in permutations(needle)])

	count=  0

	for n in poss:
		temp = ""
		for i in n:
			temp = temp+i
		if temp in haystack:
			count+= 1

	print(count)

