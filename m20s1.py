import random

n = int(input())
p1 = str.split(input(), " ")
p2 = str.split(input(), " ")

#~ done = False
nbattle = 0
#~ x = 0
#~ while done == False:
	#~ if x >= len(p1):
		#~ done = True
		#~ break
	#~ if p1[x] != p2[x]:
		#~ continue
	#~ if p1[x] == p2[x]:
		#~ nbattle = nbattle + 1
		#~ war = True
		#~ while war == True:
			#~ x += 1
			#~ if p1[x]!= p2[x]:
				#~ war = False
	#~ x += 1

ind = []	
for i in range(n):
	if p1[i] == p2[i]:
		ind.append(i)
nbattle = len(ind)
for i in range(len(ind)-1):
	if ind[i+1] - ind[i] == 1:
		nbattle -= 1
		continue

print(nbattle)
