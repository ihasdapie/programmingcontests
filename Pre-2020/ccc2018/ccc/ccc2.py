import sys
a=[]
 
for line in sys.stdin:
	a.append(line)
 
b=int(a[0])
c=a[1]
d=a[2]

cl=[]
dl=[]

out=0
for x in c:
	cl.append(x)

for x in d:
	dl.append(x)

for x in range(b):
	if cl[x] == dl[x] == 'C':
		out +=1

print out
