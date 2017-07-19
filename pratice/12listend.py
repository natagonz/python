#mengambill list index pertama dan terkahir



a = [ 1,23,9,10,11]


def new_list(x,y):
	b = []
	b.append(a[x])
	b.append(a[y])
	return b

print new_list(0,-1)