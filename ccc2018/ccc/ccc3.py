import sys

a=[]

for line in sys.stdin:
	a.append(line)

b=''
for x in range(len(a)):
	b=b+a[x]
	
b=b.split(' ')

c=[]

for x in range(len(b)):
	c.append(int(b[x]))

a=c

	

print 0, ' ', a[0], ' ', a[0] + a[1], ' ', a[0] + a[1] + a[2], ' ',a[0] + a[1] + a[2]+ a[3]
print a[0], ' ', 0, ' ', a[1],' ', a[1] + a[2],' ', a[1]+a[2]+a[3]
print a[0] + a[1],' ', a[1], ' ', 0, ' ',a[2], ' ', a[2] + a[3]
print a[0]+a[1]+a[2],' ',a[1] + a[2], ' ', a[2], ' ', 0, ' ', a[3]
print a[0]+a[1]+a[2]+a[3],' ',a[3]+a[1]+a[2], ' ',a[2]+a[3], ' ',a[3], ' ', 0 

