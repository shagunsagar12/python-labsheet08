sql = "UPDATE students SET name = %s WHERE id = %s"
cur.execute(sql, ("Aarav", 1))
con.commit()

print("Student name updated successfully!")