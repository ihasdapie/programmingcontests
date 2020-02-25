
m = int(input())
puzzle = []
for i in range(m):
	temp = str.split(input(), " ")
	temp = [int(x) for x in temp]
	puzzle.append(temp)

def flip(puzzle, r= -1, c= -1):
	if r = -1:
		for i in range(len(puzzle[c])):
			if puzzle[c][i] == "0":
				puzzle[c][i] = "1"
				
			elif puzzle[c][i] == "1":
				puzzle[c][i] = "0"
	
	if c = -1:
		for i in range(len(puzzle[0][r])):
			if puzzle[i][r] == "0":
				puzzle[i][r] = "1"
				
			elif puzzle[i][r] == "1":
				puzzle[i][r] = "0"

