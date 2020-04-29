
class turtle:
	def __init__(self, x, y, z, front = 1, leftSide= 2, top=3):
		self.x = x
		self.y = y
		self.z = z
		#+1 = +x, -1 = -x, +2 = +y, -2 = -y...
		self.front = front
		self.leftSide = leftSide
		self.top = top
	def getCoords(self):
		return((self.x, self.y, self.z))

def calcDist(x1, y1, z1, x2, y2, z2):
	return (((x2-x1)**2)+((y2-y1)**2)+((z2-z1)**2))**0.5

def spc(a1, a2, pa):
	#the distance perpendicular to the plane of movement is irrelevant
	#return point in axis of movement that gives the lowest distance
	if pa in range(a1, a2):
		return(pa)
	else:
		if abs(a1-pa) <= abs(a2-pa):
			return(a1)
		else:
			return(a2)		


#~ def spc(a1, b1, a2, b2, pa, pb):
#~ if pa in range(a1, a2):
		#~ return((pa, b1)) 
	#~ elif pb in range(b1, b2):
		#~ return((a1, pb))	
	#~ else:
		#~ if (a1-a2) == 0:
			#~ if abs(b1-pb) <= abs(b2-pb):
				#~ return((a1, b1))
			#~ else:
				#~ return((a1, b2))		
		#~ else:
			#~ if abs(a1-pa) <= (a2-pa):
				#~ return((a1, b1))
			#~ else:
				#~ return((a1, b1))
		
		

startPoint=str.split(input(), " ")
startPoint=[int(x) for x in startPoint]
spaceTurtle = turtle(startPoint[0], startPoint[1], startPoint[2])
planetLoc = str.split(input(), " ")
planetLoc = [int(x) for x in planetLoc]

listActions = []

done = False

lowestDistance = 10000.0

while done == False:
	a = str.split(input(), " ")
	a[0] = int(a[0])
	if a[1] == "E":
		listActions.append(a)
		done = True
	else:
		listActions.append(a)

#~ print(calcDist(planetLoc[0], planetLoc[1], planetLoc[2], spaceTurtle.x, spaceTurtle.y, spaceTurtle.y))

for p in listActions:
	
	iLoc = spaceTurtle.getCoords()
	#apply movement
	if spaceTurtle.front == 1:
		spaceTurtle.x += p[0]
	elif spaceTurtle.front == 2:
		spaceTurtle.y += p[0]
	elif spaceTurtle.front == 3:
		spaceTurtle.z += p[0]
		
		
	elif spaceTurtle.front == -1:
		spaceTurtle.x -= p[0]
	elif spaceTurtle.front == -2:
		spaceTurtle.y -= p[0]
	elif spaceTurtle.front == -3:
		spaceTurtle.z -= p[0]
		
	#apply rotation
	
	cFront =  spaceTurtle.front
	cleftSide = spaceTurtle.leftSide
	cTop = spaceTurtle.top
	
	rot = p[1]
	
	if rot == "L":
		spaceTurtle.front = cleftSide
		spaceTurtle.leftSide = (cFront)*-1
	elif rot == "R":
		spaceTurtle.front = cleftSide*-1
		spaceTurtle.leftSide = cFront
	elif rot == "U":
		spaceTurtle.front = cTop
		spaceTurtle.top = cFront*-1
	elif rot == "D":
		spaceTurtle.front = cTop*-1
		spaceTurtle.top = cFront
	
	fLoc = spaceTurtle.getCoords()
	
	dLoc = [fLoc[x]-iLoc[x] for x in range(3)]
	
	if dLoc[0] != 0:
		#moving in x
		
		tx = spc(iLoc[0], fLoc[0], planetLoc[0])
		a = calcDist(planetLoc[0], planetLoc[1], planetLoc[2], tx,  spaceTurtle.y, spaceTurtle.z)
		#~ print("x", spaceTurtle.x, ty, tz, a)
					
	elif dLoc[1] != 0:
		#moving in y
		
		ty = spc(iLoc[1], fLoc[1], planetLoc[1])
		#~ tx, tz = spc(iLoc[0], iLoc[2], fLoc[0], fLoc[2], planetLoc[0], planetLoc[2])
		a = calcDist(planetLoc[0], planetLoc[1], planetLoc[2], spaceTurtle.x, ty, spaceTurtle.z)
		#~ print("y", tx, spaceTurtle.y, tz, a)
					

	elif dLoc[2] != 0:
		#moving in z
		
		tz = spc(iLoc[2], fLoc[2], planetLoc[2])
		#~ tx, ty = spc(iLoc[0], iLoc[1], fLoc[0], fLoc[1], planetLoc[0], planetLoc[1])
		a = calcDist(planetLoc[0], planetLoc[1], planetLoc[2], spaceTurtle.x, spaceTurtle.y, tz)
		#~ print("z", tx, ty, spaceTurtle.z, a)
					

	#~ print("spaceTurtle: ", spaceTurtle.x, spaceTurtle.y, spaceTurtle.z)
	#~ print("path distance: ", a)
	#~ print("")
	if a<lowestDistance:
		lowestDistance = a
		
ld = str(round(lowestDistance, 2))

if ld[-3] == ".":
	print(ld)
else:
	print(ld+"0")



