cur.execute("SELECT * FROM students")

for row in cur.fetchall():
    print(row)