#menebak nomor dalam 1 sampai 9


""" fitur :
1.bermain ulang
2. menebak kalau lbh rendah print tebakan terlalu rendah dan sebaliknya

lets do it """


from random import randint

play_again = "yes"

while play_again == "yes" :
	number = randint(1,9)
	guess = int(raw_input("Pilih nomor 1 sampai 9 : "))
	
	if number == guess :
		print " Tebakan anda benar"

	elif guess > number :
		print " Tebakan anda terlalu tinggi, tebakan yang benar adalah %s" %(number)

	else :
		print " Tebakan anda terlalu rendah, tebakan yang benar adalah %s" %(number)


	play_again = raw_input("play again ? ")