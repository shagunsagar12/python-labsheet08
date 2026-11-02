import csv

with open("students.csv", "r", newline="") as file:
    reader = csv.DictReader(file)

    data = [
        (int(row["id"]), row["name"],
         int(row["age"]), float(row["marks"]))
        for row in reader
    ]

cur.executemany("""
INSERT INTO students (id, name, age, marks)
VALUES (%s, %s, %s, %s)
""", data)

con.commit()
print(len(data), "records imported successfully!")