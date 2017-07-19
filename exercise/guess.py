import random 

a = random.randint(1,9)

play_again = "yes"

while play_again == "yes" :
	guess = int(raw_input("tebak angka "))
	if guess < a :
		print "Tebakan terlalu rendah "
	elif guess > a :
		print "Tebakan terlalu tinggi "
	else :
		print " Yak benar"

	play_again = raw_input("main lagi yes/no : ")