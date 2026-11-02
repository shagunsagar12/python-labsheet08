cur.execute("""
SELECT age, COUNT(*)
FROM students
GROUP BY age
ORDER BY age
""")

for row in cur.fetchall():
    print("Age:", row[0], "Count:", row[1])