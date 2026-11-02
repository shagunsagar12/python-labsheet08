cur.execute("SELECT name, marks FROM students")

for row in cur.fetchall():
    print(row)