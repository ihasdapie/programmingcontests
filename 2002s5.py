#~ #n, m is the dimensions of the screen
#~ #startingPoint is the point along the bottom (n) that the ball starts at
#~ #firstBounce is the point along the right wall that the ball first hits

width = int(input())
height = int(input())
startPoint = int(input()) 
firstBounce = int(input()) #right wall

#5x5 box on the edges -> end loop
#how to tell if it never will go in? -> 

slope = firstBounce/(width-startPoint)
#find y intercept
b = -slope*(startPoint)
x = 2*width
count = 0
while True:
	y = slope*x + b
	if y%height < 5 or y%height > (width-5):
		if y%height == 0:
			count = x//width + int(y/height)-2
		else:
			count = x//width + int(y/height)-1
		break
	if y%height == firstBounce:
		count = 0
		break
	x += width
	
print(count)

