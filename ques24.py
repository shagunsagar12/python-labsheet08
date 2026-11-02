cur.execute("SELECT AVG(marks) FROM students")

result = cur.fetchone()
print("Average marks:", result[0])