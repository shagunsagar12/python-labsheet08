cur.execute("DELETE FROM students WHERE id = %s", (5,))
con.commit()

print(cur.rowcount, "record deleted")