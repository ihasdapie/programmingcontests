j = int(input())
a = int(input())
js = []
al = []

n = 0
for i in range(j):
	#set as 1 if it is taken
	js.append([input(), 0])
for i in range(a):
	al.append(str.split(input(), " "))


def sztonum(sz):
	if sz == "S":
		return(1)
	elif sz == "M":
		return(2)
	else:
		return(3)

for a in range(len(al)):
	reqsize = al[a][0]
	reqnum = int(al[a][1])
	
	jsize = js[reqnum][0]
	if js[reqnum][1] == 1:
		continue
	else:
		if sztonum(reqsize) > sztonum(jsize):
			continue
		elif sztonum(reqsize) < sztonum(jsize):
			js[reqnum][1] = 1
			n += 1
		if jsize == reqsize:
			js[reqnum][1] = 1
			n += 1

print(n)
