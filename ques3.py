import mysql.connector

con = mysql.connector.connect(
    host="localhost",
    user="root",
    password="7906Sa@12",
    database="college"
)

cur = con.cursor()