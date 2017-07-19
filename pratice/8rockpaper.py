play_again = "yes"


while play_again == "yes":
	a = raw_input("gunting,batu atau kertas ?")
	b = raw_input("gunting,batu atau kertas ?")

	if a == b :
		print "Hasil Imbang"

	elif a == "gunting" :
		if b == "kertas" :
			print "a menang"
		else :
			print "b menang"

	elif a == "batu" :
		if b == "gunting" :
			print "a menang"
		else :
			print "b menang"

	elif a == "kertas" :
		if b == "batu" :
			print "a menang"
		else :
			print "b menang"

	else :
		print " Masukan batu,gunting,kertas !!!!"

	play_again = raw_input("play again ? yes/no")
	