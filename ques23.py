cur.execute("""
SELECT students.name, courses.course_name
FROM students
LEFT JOIN courses
ON students.id = courses.student_id
""")

for row in cur.fetchall():
    print(row)