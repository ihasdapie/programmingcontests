from math import ceil
gsize = int(input())
npeople = int(input())

plist = []

for i in range(npeople):
	name = str(input())
	time = int(input())
	plist.append((name, time))

pgs = [i+1 for i in range(gsize)] #possible group sizes


pgss = [] #for generation

for i in range(int(ceil(npeople/gsize))):
	pgss += pgs


def findtime(combs):
	times = 0
	
	curind = 0
	for group in combs:
		times = times + (max([i[1] for i in plist[curind:curind+group]]))
		curind += group

	return times
	


def findcomb(numbank, target, output, mintime, partial = []):
	s = sum(partial)
	if s == target:
		t = findtime(partial)
		
		if t <= mintime:	
			output.append(partial)
			return
			
		else:
			return
	if s >= target:
		return
	for i in range(len(numbank)):
		n = numbank[i]
		remaining = numbank[i+1:]
		findcomb(remaining, target, output, mintime, partial + [n])


ming = [gsize for g in range(npeople//gsize)]
ming.append(npeople-sum(ming))
mintime = findtime(ming)

combs = []
findcomb(pgss, npeople, combs, mintime)

#~ def findcomb(numbank, target, output, partial = []):
	#~ s = sum(partial)
	#~ if s == target:
		#~ output.append(partial)
		#~ return
	#~ if s >= target:
		#~ return
	#~ for i in range(len(numbank)):
		#~ n = numbank[i]
		#~ remaining = numbank[i+1:]
		#~ findcomb(remaining, target, output, partial + [n])


#~ combs = []
#~ findcomb(pgss, npeople, combs)






for x in combs:
	
	a = findtime(x)
	if a <= mintime:
		mincomb = x
		mintime = a

print("Total Time: " + str(mintime))




curind = 0
for group in mincomb:
	k = ""
	for person in range(group):
		k = k + plist[curind][0] + " "
		curind += 1
	print(k)
	
