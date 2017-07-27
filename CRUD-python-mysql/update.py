import MySQLdb as mdb
import sys

#update user

con = mdb.connect('localhost','root','root','python');#masukan database password,username,table
cur = con.cursor()

sql = "UPDATE user SET nama = '%s' WHERE `id` = '%s'" %("natadestroyer", 1)

try:
	cur.execute(sql) #eksekusi
	con.commit()#simpan ke dataabse
	print "Success"
	print cur._last_executed

except:
	con.rollback()
	print "fail"

if con:
	con.close()
