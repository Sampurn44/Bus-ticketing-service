import  sqlite3
conn=sqlite3.connect("student.db")
print("Database Opened successfully")
conn.execute("""
CREATE TABLE ADMIN(
ADMIN_ID INTEGER PRIMARY KEY AUTOINCREMENT  NOT NULL ,
USERNAME TEXT NOT NULL, 
PASSWORD TEXT NOT NULL)
""")
print ("Table ADMIN created successfully")
