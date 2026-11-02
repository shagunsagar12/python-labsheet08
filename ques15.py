cur.execute("""
SELECT * FROM students
ORDER BY marks DESC
LIMIT 3
""")

for row in cur.fetchall():
    print(row)