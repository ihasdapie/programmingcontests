#2002 S4- Spreadsheet

row = {0:"A", 1:"B", 2:"C", 3:"D", 4:"E", 5:"F", 6:"G", 7:"H", 8:"I", 9:"J"}
sheet = {}
#~ def fill(current, path = [], s = 0, ind = 0):
	#~ global sheet
	#~ global row
	
	#~ if False in [str.isdigit(x) for x in path] == False:
	#~ if sheet[current].celltype == "num":
		#~ print(current, sheet[current].value)
		#~ return
		
	#~ if sheet[current].celltype == "path":
		#~ path = sheet[current].value
		#~ for p in range(len(path)):
			#~ if sheet[path[p]].celltype == "num":
				#~ s = s+ sheet[path[p]].value
				#~ fill(path[:], 
			#~ elif sheet[path[p]].celltype == "path":
				#~ if p in sheet[path[p]].value:
					#~ return
				#~ else:
					#~ fill(path[p], path[p:], s, ind+1)

		#~ for p in range(len(path)):
			

#~ def fill(original, path, s=0):
	#~ global sheet
	
	#~ if original in path:
		#~ sheet[original] = "*"
		#~ return
	
	
	#~ if len(path) == 0:
		#~ sheet[original] = s
		#~ return
		
	#~ for c in path:
		#~ if sheet[c].celltype == "num":
			#~ s = s + sheet[c].value
		#~ else:
			#~ fill(original, sheet[c].value, s)
				

	
	
	
	
	
	
	
	
	

class cell:
	def __init__(self, celltype, value = -1, path = []):
		#celltype num, path
		self.celltype = celltype
		self.value = value
		self.path = path

# -> 9x (1-9)
# up/down 10x (A-J)


for x in range(10):
	temp = str(input()).split(" ")
	for y in range(len(temp)):
		if str.isdigit(temp[y]) == True:
			sheet[row[x]+str(y+1)] = (cell("num", value = int(temp[y])))
		else:
			#path will be split at "+" for convenience
			sheet[row[x]+str(y+1)] = cell("path", path = str.split(temp[y], "+"))


#try using iteration				

#~ print(sheet["A4"].value)	

nochanges = False

while nochanges != True:
	nochanges = True
	for x in range(10):
		for y in range(1,9):
			a = str(row[x]+str(y))
			if sheet[a].celltype == "path":
				#if there is a path given..
				nochanges = False
				path = sheet[a].path
				np = []
				
				#iterate over path to see what values there are
				#check if there is a null here.
				
				if a in path:
					sheet[p].value = "*"
					sheet[p].celltype = "null"
				
				#now, if there is no null, expand on the path
								
				else:
					for p in path:
						np.append(sheet[p].value)
				
				#add values and paths to np; new path
				
				#look at the new path and give it a list with the nums and paths
				
					d = [type(x) for x in np]
					if str in d == False and list in d == False:
						#if the list of paths has terminated(only int left), sum and set value
						sheet[p].value = sum(np)
						sheet[p].celltype = "num"
				
					else:
						#if the list of paths has not been terminated, set the 'new path'
						sheet[p].value=sum([x for x in np if type(x) == int])
						for s in np:
							if type(s) == list:
								np.remove(s)
								for i in s:
									np.append(s)
							elif type(s) == int:
								np.remove(s)
			
						
						
#print out sheet as it was when inputted
