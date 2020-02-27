import sys

sys.setrecursionlimit(100000)


"""

base case: len(rb) == 1 -> riceball size = rn[0]

rb1 = rb2 (adjacent)->combine in place
rb1 != rb2 != rb3 -> rb1 = rb4 -> combine all three

1. find possible moves
2. apply each one of the moves -> create new array
3. find possible moves for each new array
4. repeat

how to memoize?

this task ends up reducing into arrays that can be mapped to a max.
memoize each array to a max
"""

maxMem = {}
#key: array, value = max

#~ arrMem = {}
#key: array, value = array
#value is the possible arrays that may arise from the key array

pMoveMem = {}
#format of a move: (ind1, ind2) 

def findLargestComb(rbArray, maxN):
	#base case: no more moves to make
	global maxMem
	#~ global arrMem
	tempRbTuple = tuple(rbArray)
	#~ print(rbArray)
	if maxMem.get(tempRbTuple) != None:
		if maxMem[tempRbTuple]>maxN:
			maxN = maxMem[tempRbTuple]
			return
					
	elif len(findPossibleMoves(rbArray)) == 0:
		maxMem[tempRbTuple] = max(rbArray)
		if maxMem[tempRbTuple] > maxN:
			maxN = maxMem[tempRbTuple]
			return
			
	else:
		mList = findPossibleMoves(rbArray)
		for move in mList:
			findLargestComb(applymove(rbArray, move),maxN)


def findPossibleMoves(rbArray):
	#memoized
	#returns an array of tuples of possible moves
	global pMoveMem
	tempRbTuple = tuple(rbArray)

	if pMoveMem.get(tempRbTuple) != None:
		return pMoveMem[tempRbTuple]
	
	else:
		mList = []
		for i in range(len(rbArray)-1):
	
			if rbArray[i] == rbArray[i+1]:
				mList.append((i, i+1))
				
			if i <= len(rbArray)-3:
				if rbArray[i] == rbArray[i+2]:
					mList.append((i, i+2))
		pMoveMem[tempRbTuple] = mList
		return pMoveMem[tempRbTuple]
		
		
		
def applymove(riceBalls, inds):
	#note that applying moves will shift things: can only apply one move per array
	#returns a new array after moves have been applied
	rbArray = riceBalls.copy()
	ind1 = inds[0]
	ind2 = inds[1]
	if (ind2-ind1) == 2:
		#three items
		rbArray[ind1] = rbArray[ind1]+rbArray[ind2] + rbArray[ind1+1] #this is the inbetween value
		rbArray.pop(ind2)
		rbArray.pop(ind1+1)
		return rbArray
		
	elif (ind2-ind1) == 1:
		#two items
		rbArray[ind1] = rbArray[ind1] + rbArray[ind2]
		rbArray.pop(ind2)
		return rbArray
	else:
		print("ApplyMoveError")

n = int(input())
riceBalls = [int(x) for x in str.split(input(), " ")]


#~ print("RiceBalls: ",riceBalls)
maxN = -1
#~ print(findPossibleMoves(riceBalls))
findLargestComb(riceBalls, maxN)

#~ print(maxMem)
print(max(maxMem.values()))
