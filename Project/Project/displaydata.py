#import library
import sqlite3
#open database
conn = sqlite3.connect('student.db')
#display recrod
cursor = conn.execute("SELECT * from ADMIN")
print("ID\tUSERNAME\tPASSWORD")
for row in cursor:
   print ("{}\t{}\t\t{}".format(row[0],row[1],row[2]))
conn.close()
