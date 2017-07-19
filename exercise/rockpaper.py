play_again = "yes"

while play_again == "yes" :
	guess1 = raw_input("pilih kertas,gunting,batu : ")
	guess2 = raw_input("pilih kertas,gunting,batu : ")

	if  guess1 == guess2 :
		print "hasil imbang"

	elif guess1 == "kertas":
		if guess2 == "gunting":
			print "gunting menang"
		else : 
			print "Kertas menang"

	elif guess1 == "gunting":
		if guess2 == "batu":
			print "batu menang"
		else :
			print "gunting menang"

	elif guess1 == "batu":
		if guess2 == "kertas":
			print "kertas menang"
		else :
			print "batu menang"
	else :
		print " Masukan kertas,atau gunting !!!"

	play_again = raw_input(" main lagi ? yes/no : ")