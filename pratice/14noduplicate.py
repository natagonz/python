a = [1,1,2,2,3,4,4,5,6,6,8]


def no_duplicate(x):
	x = list(set(x))
	return x

print no_duplicate(a)