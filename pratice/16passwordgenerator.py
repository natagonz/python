import random

a = "yes"

while a == "yes":
	password = "1  2 3   4 5   6 7 89 h gv vh j s y h j 3 7 7 3 7 7 & & & W @ & & & E T   ^ % # # % # # $ ^##  P # # O # {# # # * #  &  # & # & # & # &#&#&(!))!))!*!)*#*#( # D  H fg& &T&T @T@ TEE"
	user = raw_input("mau password yang lemah atau kuat")
	
	if user == "lemah":
		newpass = "".join(random.sample(password,10))
		print newpass
	
	elif user == "kuat" :
		newpass = "".join(random.sample(password,20))
		print newpass

	a = raw_input("ulangi ? ")

