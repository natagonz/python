word = "aku sayang virania"

def reverse(x):
	x = x.split()
	#x = x[::-1]
	x.reverse()
	return x

print reverse(word)