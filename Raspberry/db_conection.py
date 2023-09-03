import MySQLdb

db = MySQLdb.connect('birzyay0v1nhjnvywaun-mysql.services.clever-cloud.com', 'ud03785zpvgrc7vl', 'a40n0YCYBLlPTdts4wln', 'birzyay0v1nhjnvywaun')

cur = db.cursor()

cur.execute("SELECT * FROM Admins_space")

for row in cur.fetchall():
	print(row[1])
