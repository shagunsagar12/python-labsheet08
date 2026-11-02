cur.execute("DESCRIBE students")

for row in cur.fetchall():
    print(row)