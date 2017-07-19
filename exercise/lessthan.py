a = [ 1,2,3,4,5,6,7,101,33,22,33,1,22,33,44,9]

b = []

for x in a :
	if x < 10:
		b.append(x)

for i in b :
	print "number di b " + str(i)

print b
