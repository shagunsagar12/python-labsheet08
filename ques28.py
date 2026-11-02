import mysql.connector

try:
    con = mysql.connector.connect(
        host="localhost",
        user="root",
        password="YOUR_PASSWORD",
        database="college"
    )

    cur = con.cursor()
    cur.execute("SELECT * FROM students")

    for row in cur.fetchall():
        print(row)

except mysql.connector.Error as e:
    print("Database error:", e)

finally:
    if "cur" in locals():
        cur.close()

    if "con" in locals() and con.is_connected():
        con.close()