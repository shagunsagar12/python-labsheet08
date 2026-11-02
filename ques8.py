sql = """
INSERT INTO students (id, name, age, marks)
VALUES (%s, %s, %s, %s)
"""

data = (1, "Aman", 20, 85)

cur.execute(sql, data)
con.commit()

print("Record inserted successfully!")