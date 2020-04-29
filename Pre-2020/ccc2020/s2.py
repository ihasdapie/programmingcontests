

m = int(input())
n = int(input())

room = []
for i in range(m):
	room.append([int(x) for x in str.split(input(), " ")])


locMem = {}
#store a (r,c) and possible factorizations

fMem = {}
#int, list of tuple (f1, f2)
def factors(i):
	if i in fMem:
		return fMem[i]
	else:
		fList = []
		for x in range(1, i+1):
			if i%x == 0:
				fList.append((x, i//x))
		fMem[i] = fList
		return fMem[i]
		
def filterFactors(f, m, n):
	nl = []
	for x in f:
		if x[0] <= m and x[1] <= n:
			nl.append(x)
	return nl	
	




#the two above give the possible jump locations from an int value on the grid
#go through each of the possible jump locations
	
currPos = (1,1)

done = False
#set upper limit to 400k for now

def runMoves(pos, graph, count):
	print(pos)
	if count >= 10:
		return "no"
	if pos == (m, n):
		return "yes"
	else:
		moves = factors(graph[pos[0]-1][pos[1]-1])
		moves = filterFactors(moves, m, n)
		if ((m, n) in moves == True):
			print("a", count)
			return "yes"
		
		else:
			print("b", count)
			for move in moves:
				runMoves(move, graph, count+1)




def runMoves(pos, graph, count, p = []):
	moves = factors(graph[pos[0]-1][pos[1]-1])
	moves = filterFactors(moves, m, n)
	#~ print(moves)
	if len(p) >= 1:
		return
	
	elif (m,n) in moves:
		p.append(True)
		return
	elif count >= 10:
		return
	else:
		if len(moves) == 0:
			return
		else:
			for move in moves:
				runMoves(move, graph, count+1, p)

p = []


if m == 2:
	if room[m-1][n-1]%2 != 0:
		print("yes")
	else:
		print("no")
		
elif m == 1:
	f = factors(room[0][0])
	if (1,n) in f:
		print("yes")
	else:
		print("no")


else:
	runMoves(currPos, room, 0, p)
	if True in p:
		print("yes")
	else:
		print("no")
