import mysql.connector

try:
    con = mysql.connector.connect(
        host="localhost",
        user="root",
        password="7906Sa@12"
    )

    if con.is_connected():
        print("Database connected successfully!")

    con.close()

except mysql.connector.Error as e:
    print("Error:", e)