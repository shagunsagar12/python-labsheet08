def insert_student(cur, con, student):
    sql = """
    INSERT INTO students (id, name, age, marks)
    VALUES (%s, %s, %s, %s)
    """
    cur.execute(sql, student)
    con.commit()
    print("Student inserted successfully!")

def fetch_students(cur):
    cur.execute("SELECT * FROM students")

    for row in cur.fetchall():
        print(row)

# Function calls
insert_student(cur, con, (20, "Meena", 20, 91))
fetch_students(cur)