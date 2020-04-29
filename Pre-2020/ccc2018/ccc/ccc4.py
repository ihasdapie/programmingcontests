import sys

a=[2, [1,3], [2,9]]
print a
'''
for line in sys.stdin:
	a.append(line)
'''
pt1=a[1][0]
pt2=a[1][-1]
pt3=a[-1][0]
pt4=a[-1][-1]


#find relationships between each other

top=False
bottom=False
left=False
right=False
norotate=False

ptl=[pt1,pt2,pt3,pt4]

if pt2>pt1 and pt4>pt3 and pt1<pt3:
	norotate=True
	
if pt4>pt2 and pt3>pt1 and pt2<pt1:
	top=True
	
if pt3>pt4 and pt1>pt2 and pt4<pt2:
	right=True
	
if pt1>pt3 and pt2>pt4 and pt3<pt4:
	bottom=True

#~ def rotate90r(grid):
	#~ 
	

#~ def rotate90l(grid):	

def createrows(grid):
	rowlist = []
	for x in range((grid[0])):
		templist=[]
		if x != 0:
			for y in range(grid[0]):
				templist.append(grid[x][y])
				
			rowlist.append(templist)
	
	return rowlist


def rotate180tb(grid):
	for x in range((grid[0]/2)):
		grid[x] = grid[(grid[0]-x)]
	return grid

def rotate180lr(grid):
	for x in range(len(grid)):
		grid[x+1].reverse()
		return grid
	
print 'top', top, 'bottom', bottom, 'left', left, 'right', right, 'norotate', norotate

print createrows(a)







