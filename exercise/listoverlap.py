a = [1,2,3,4,5,6,7,8]
b = [1,2,3,4,5,6,7,9]

c = []
for x in a :
	if x in b:
		c.append(x)

print c