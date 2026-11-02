import csv

cur.execute("SELECT * FROM students")
rows = cur.fetchall()

with open("students.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["id", "name", "age", "marks"])
    writer.writerows(rows)

print("Data exported to students.csv")