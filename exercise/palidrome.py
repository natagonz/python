word = raw_input("enter a word ")

rsv = word[::-1]
print rsv

if word == rsv :
	print " Your word is palidrome "
else :
	print " not Palidrome "