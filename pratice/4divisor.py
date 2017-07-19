
angka = int(raw_input("masukan angka :"))

list = range(1,angka+1)
divisor = []

for x in list :
	if angka % x == 0 :
		divisor.append(x)

print divisor
