
import sys

con1=False
conmid=False
con2=False


a=[]

for line in sys.stdin:
	a.append(line)

for x in range(len(a)):
	a[x]=int(a[x])

if a[0] == 8:
	con1 = True
elif a[0] == 9:
	con1 = True
else:
	con1 = False

if a[3] == 8:
	con2 = True
elif a[3] == 9:
	con2 = True
else:
	con2 = False



if a[2] == a[1]:
	conmid= True
else:
	conmid = False


if con1 and con2 and conmid == True:
	print 'ignore'

else:
	print 'answer'
