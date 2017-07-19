"""Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the user. Hint: how does an even / odd number react differently when divided by 2?

Extras:

    If the number is a multiple of 4, print out a different message.
    Ask the user for two numbers: one number to check (call it num) and one number to divide by (check). If check divides evenly into num, tell that to the user. If not, print a different appropriate message.
"""


angka = int(raw_input("masukan angka : "))
check = int(raw_input("angka kedua :"))


if angka % 4 == 0 :
	print "angka ini kelipatan 4"
elif angka % 2 == 0 :
	print "angka ini genap"
else :
	print "angka ini ganjil"

if angka % check == 0 :
	print "hasilnya genap"
else :
	print "hasilnya ganjil" 