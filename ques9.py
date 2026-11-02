sql = """
INSERT INTO students (id, name, age, marks)
VALUES (%s, %s, %s, %s)
"""

data = [
    (2, "Riya", 21, 92),
    (3, "Rahul", 20, 75),
    (4, "Priya", 22, 88),
    (5, "Karan", 19, 35)
]

cur.executemany(sql, data)
con.commit()

print(cur.rowcount, "records inserted")