

class cell:
	def __init__(self, celltype, value = -1, path = []):
		self.value = value
		self.path = path
		self.celltype = celltype
		
sheet = []

for x in range(10):
	inputLine = str.split(str(input()), " ")
	for y in range(len(inputLine)):
		if str.isdigit(inputLine[y]) == True:
			# n for numerical, p for path
			inputLine[y] = cell("n", value = int(y))
		else:
			inputLine[y] = cell("p", path = str.split(inputLine[y], "+"))
	sheet.append(inputLine)

def retLoc(coord):
	row = {'A':0, 'B':1, 'C':2, 'D':3, 'E':4, 'F':5, 'G':6, 'H':7, 'I':8, 'J':9}
	return(row[coord[0]], int(coord[1])-1)

complete = False

while complete != True:
	complete = True
	for x in range(10):
		for y in range(9):
			#~ if sheet[x][y].path == [] and sheet[x][y].celltype == "p" #turn into num cells
			if sheet[x][y].celltype == 'n':
				continue
				
			else: # sheet[x][y].celltype == 'p':
				#operate on all the paths
				complete = False
				newPath = []
				for p in sheet[x][y].path:
					coords = retLoc(p)
					if (x, y) == coords:
						sheet[x][y].value = "*"
						sheet[x][y].celltype = "n"
						sheet[x][y].path = []
						continue
					else:	
						newPath.append(sheet[coords[0]][coords[1]].path)
				if len(newPath) == 0:
					sheet[x][y].celltype = "n"
					sheet[x][y] = []
				print(new
				#the new path will be a list of path lists and numbers.
				#take the numbers out and add them to the value
				#keep path lists around
				sheet[x][y].value = sum([x for x in newPath if type(x) == int])
				#remove ints
				newPath = [x for x in newPath if type(x) != int]
				#everything will only be one list deep, therefore only need to go down once
			
				for l in newPath:
					if type(l) == list:
						for i in l:
							newPath.append(l)
						newPath.remove(l)
