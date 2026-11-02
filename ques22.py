cur.execute("""
SELECT students.name, courses.course_name
FROM students
INNER JOIN courses
ON students.id = courses.student_id
""")

for row in cur.fetchall():
    print(row)