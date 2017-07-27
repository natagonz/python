import MySQLdb as mdb
import sys

#mengambil data hanya 1 user

con = mdb.connect('localhost','root','root','python'); #masukan database password,username,table
cur = con.cursor()

try:
	sql = "SELECT * FROM `user` WHERE `id` ='%s'" %('1') #select darai table sesuai id
	cur.execute(sql) #eksekusi
	user = cur.fetchone() #ambil satu
	print "Nama : %s " % user[1]

except :
	print "selecting database failed"

if con:
	con.close() #ttp koneksi