cur.execute("DELETE FROM students WHERE marks < %s", (40,))
con.commit()

print(cur.rowcount, "records deleted")