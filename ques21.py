cur.execute("""
CREATE TABLE IF NOT EXISTS courses (
    course_id INT PRIMARY KEY,
    student_id INT,
    course_name VARCHAR(50),
    FOREIGN KEY (student_id) REFERENCES students(id)
)
""")

data = [
    (101, 1, "Python"),
    (102, 2, "SQL"),
    (103, 3, "Java")
]

cur.executemany("""
INSERT IGNORE INTO courses
(course_id, student_id, course_name)
VALUES (%s, %s, %s)
""", data)

con.commit()
print("Courses table created and data inserted!")