cur.execute("SHOW TABLES LIKE 'students'")

if cur.fetchone():
    print("Table exists")
else:
    print("Table does not exist")