y = int(input())
x = int(input())
byard = []
for i in range(y):
	byard.append(str(input()))

num_dir = int(input())

moves = []

for i in range(num_dir):
	moves.append(str(input()))
	
locations = []
# (y, x) format - list of tuples

#find locations

for i in range(len(byard)):
	for j in range(len(byard[i])):
		if byard[i][j] == ".":
			locations.append((i, j))

def applymoves(yard, moves, mi, direction, sloc):
	#sloc = starting location
	#mi -> move index
	#exit condition when moveindex == len(moves) and final location is valid, return location
	#exit condition when location is not valid - return f
	
	if (mi) == len(moves):
		return(sloc)
	
	elif direction == 'n':
		if moves[mi] == 'F':
			if sloc[0]-1 >= 0:
				if yard[sloc[0]-1][sloc[1]] != 'X':
					return applymoves(yard, moves, mi + 1, direction, (sloc[0]-1, sloc[1]))
				else:
					return 'f'
			else:
				return 'f'
				
		elif moves[mi] == 'L':
			return applymoves(yard, moves, mi + 1,  'w', sloc)
		elif moves[mi] == 'R':
			return applymoves(yard, moves, mi + 1,  'e' , sloc)
		
		
		
	elif direction == 'e':
		if moves[mi] == 'F':
			if sloc[1]+1 <= len(yard[0])-1:
				if yard[sloc[0]][sloc[1]+1] != 'X':
					return applymoves(yard, moves, mi + 1, direction, (sloc[0], sloc[1]+1)) 
				else:
					return 'f'
			else:
				return 'f'
				
		elif moves[mi] == 'L':
			return applymoves(yard, moves, mi + 1, 'n', sloc)
		elif moves[mi] == 'R':
			return applymoves(yard, moves, mi + 1,  's' , sloc)

	elif direction == 's':
		if moves[mi] == 'F':
			if sloc[0]+1 <= len(yard)-1:
				if yard[sloc[0]+1][sloc[1]] != 'X':
					return applymoves(yard, moves, mi + 1, direction,  (sloc[0]+1, sloc[1])) 
				else:
					return 'f'
			else:
				return 'f'
				
		elif moves[mi] == 'L':
			return applymoves(yard, moves, mi + 1,  'e', sloc)
		elif moves[mi] == 'R':
			return applymoves(yard, moves, mi + 1,  'w' , sloc)

	elif direction == 'w':
		if moves[mi] == 'F':
			if sloc[1]-1 >= 0:
				if yard[sloc[0]][sloc[1]-1] != 'X':
					return applymoves(yard, moves, mi + 1, direction, (sloc[0], sloc[1]-1)) 
				else:
					return 'f'
			else:
				return 'f'
				
		elif moves[mi] == 'L':
			return applymoves(yard, moves, mi + 1, 's', sloc)
		elif moves[mi] == 'R':
			return applymoves(yard, moves, mi + 1, 'n' , sloc)




results = []
for spoint in locations:
	results.append(applymoves(byard, moves, 0, 'n', spoint))
	results.append(applymoves(byard, moves, 0, 'e', spoint))
	results.append(applymoves(byard, moves, 0, 's', spoint))
	results.append(applymoves(byard, moves, 0, 'w', spoint))

results = filter(lambda i: isinstance(i, tuple), results)

for i in results:
	a = list(byard[i[0]])
	a[i[1]] = "*"
	b = ""
	b = b.join(a)
	byard[i[0]] = b
	

for i in byard:
	print(i)


	
