from itertools import product

#~ inputa = []
#~ for line in sys.stdin:
    #~ inputa.append(line)

#~ values= [int(inputa[0]), int(inputa[1]), int(inputa[2]), int(inputa[3])]
#~ #pink, green, red, orange

pink = input()
green = input()
red = input()
orange = input()

rmoney = int(input())

values = [int(pink), int(green), int(red), int(orange)]

numtickets = [0,0,0,0]
#pink, green, red, orange

pcomb = []

leastvalue = min(values)
maxticket = (rmoney//leastvalue)+1

tcomb = product(range(maxticket), repeat = 4)
tcomb = [list(x) for x in tcomb]

for x in tcomb:
	if sum([a*b for a,b in zip(values, x)]) == rmoney:
		pcomb.append(x)

	
for x in pcomb:
    print("# of PINK is " + str(x[0]) + " # of GREEN is " + str(x[1]) + " # of RED is " + str(x[2])+ " # of ORANGE is " + str(x[3]))

print("Total combinations is "+ str(len(pcomb)) + ".")

print("Minimum number of tickets to print is " + str(min([sum(x) for x in pcomb])) + ".")

