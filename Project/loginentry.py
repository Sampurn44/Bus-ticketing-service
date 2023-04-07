import  sqlite3
conn=sqlite3.connect("student.db")
print("Database Opened successfully")

conn.execute("INSERT INTO ADMIN(USERNAME,PASSWORD) VALUES ('sampurn', '120400119')");

conn.execute("INSERT INTO ADMIN(USERNAME,PASSWORD) VALUES ('nilesh', '123')");

conn.commit()
print ("Records inserted successfully")
conn.close()
