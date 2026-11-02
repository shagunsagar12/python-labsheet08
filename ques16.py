sql = "UPDATE students SET marks = %s WHERE id = %s"
cur.execute(sql, (95, 1))
con.commit()

print(cur.rowcount, "record updated")