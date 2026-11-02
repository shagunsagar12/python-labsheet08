cur.execute("SELECT * FROM students ORDER BY marks DESC")

for row in cur.fetchall():
    print(row)