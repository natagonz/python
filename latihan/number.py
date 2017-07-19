import random

y = random.randint(1,2)

def number(angka):
	if angka == y :
		return "you win"
	else :
		return "you lose the number is %s" %(y)

print number(int(raw_input("add your guess")))
