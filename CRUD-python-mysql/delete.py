import MySQLdb as mdb
import sys

con = mdb.connect('localhost','root','root','python');#masukan database password,username,table
cur = con.cursor()



#menghapus

sql = "DELETE FROM `user` WHERE `id` = '%s'" %("3")

try:
	cur.execute(sql)#eksekusi
	con.commit()#simpan 
	print "Sukses"
	print cur._last_executed

except :
	con.rollback()
	print "faiil"

if con :
	con.close()