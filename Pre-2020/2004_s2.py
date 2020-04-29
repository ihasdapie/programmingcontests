

numYodel, numRound = input().split(" ")
numYodel, numRound = int(numYodel), int(numRound)

class yodeler:
	def __init__(self, number, score, lowestrank):
		self.number = number
		self.score = score
		self.lowestrank = lowestrank
	
	def printattributes(self):
		print("Number: ", self.number, "Score: ", self.score, "L. Rank: ", self.lowestrank)
	
	def retattributes(self):
		return ["Number: ", self.number, "Score: ", self.score, "L. Rank: ", self.lowestrank]
	
yodelList = []
for i in range(1, numYodel+1):
	yodelList.append(yodeler(i, 0, numYodel + 100))


#can sort yodellist by number in order to get their rank


roundList = []
for i in range(numRound):
	roundList.append(input().split(" "))

def sortbyscore(a):
	return a.score
def sortbynumber(a):
	return a.number
c = True
for r in roundList:
	#run a round	
	for s in range(numYodel):
		yodelList[s].score = yodelList[s].score + int(r[s])
	#update rankings
	yodelList = sorted(yodelList, key = sortbyscore, reverse = True)
	if c == True:
		for y in range(len(yodelList)):
			yodelList[y].lowestrank = y+1
		c = False
	else:
		
		for y in range(len(yodelList)):
			if yodelList[y].lowestrank < y+1:
				yodelList[y].lowestrank = y+1
	yodelList = sorted(yodelList, key = sortbynumber)
	


#print output

yodelList = sorted(yodelList, key = sortbyscore, reverse = True)

topY = []
ts = yodelList[0].score
for y in yodelList:
	if y.score == ts:
		topY.append(y)

topY = sorted(topY, key = sortbynumber)

for y in topY:
	print("Yodeller "+str(y.number)+" is the TopYodeller: score "+str(y.score)+", worst rank "+str(y.lowestrank))


