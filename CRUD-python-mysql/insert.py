import MySQLdb as mdb
import sys

#memasukan data

con = mdb.connect('localhost','root','root','python');#masukan database password,username,table
cur = con.cursor()

sql = "INSERT INTO `user` (`id`, `nama`) VALUE ('%s', '%s')" % (0, 'gon')

try :
	cur.execute(sql) #eksekusi
	con.commit() #commit ke database
	print "Input berhasil"
	print cur._last_executed

except :
	con.rollback()
	print "failed"



if con:
	con.close()