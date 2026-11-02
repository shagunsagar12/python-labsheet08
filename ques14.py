cur.execute("SELECT COUNT(*) FROM students")

result = cur.fetchone()
print("Total students:", result[0])