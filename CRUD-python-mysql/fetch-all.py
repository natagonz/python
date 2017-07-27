import MySQLdb as mdb
import sys

#ambil data semua user 

con = mdb.connect('localhost','root','root','python');#masukan database password,username,table
cur = con.cursor()

try:
	sql = "SELECT * FROM `user`"#select darai table 
	cur.execute(sql) #eksekusi
	user = cur.fetchall() #ambil semua

	for val in user : #looping user
		print "Nama : %s " % val[1] 

except :
	print "selecting database failed"

if con:
	con.close()