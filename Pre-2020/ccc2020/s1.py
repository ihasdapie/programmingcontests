n = int(input())
obs = []
for i in range(n):
	obs.append([int(x) for x in str.split(input(), " ")])

def f(a, b):
	return a[0]<b[0]

def ff(a):
	return a[0]
obs.sort(key = ff)

maxSpeed = -1

for i in range(len(obs)-1):
	s = abs((obs[i+1][1] - obs[i][1]) / (obs[i+1][0] - obs[i][0]))
	
	if s > maxSpeed:
		maxSpeed = s

print(maxSpeed)



