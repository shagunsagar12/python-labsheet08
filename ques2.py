import mysql.connector

con = mysql.connector.connect(
    host="localhost",
    user="root",
    password="7906Sa@12"
)

cur = con.cursor()
cur.execute("CREATE DATABASE IF NOT EXISTS college")

print("Database created successfully!")

cur.close()
con.close()