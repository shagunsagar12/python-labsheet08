cur.execute("SELECT * FROM students WHERE marks > 80")

for row in cur.fetchall():
    print(row)