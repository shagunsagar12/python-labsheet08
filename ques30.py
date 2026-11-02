import mysql.connector

try:
    con = mysql.connector.connect(
        host="localhost",
        user="root",
        password="YOUR_PASSWORD",
        database="college"
    )

    cur = con.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS students (
        id INT PRIMARY KEY,
        name VARCHAR(50),
        age INT,
        marks FLOAT
    )
    """)

    while True:
        print("\n--- STUDENT MANAGEMENT SYSTEM ---")
        print("1. Add Student")
        print("2. View Students")
        print("3. Update Marks")
        print("4. Delete Student")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            sid = int(input("Enter ID: "))
            name = input("Enter Name: ")
            age = int(input("Enter Age: "))
            marks = float(input("Enter Marks: "))

            cur.execute("""
            INSERT INTO students (id, name, age, marks)
            VALUES (%s, %s, %s, %s)
            """, (sid, name, age, marks))

            con.commit()
            print("Student added successfully!")

        elif choice == "2":
            cur.execute("SELECT * FROM students")

            for row in cur.fetchall():
                print(row)

        elif choice == "3":
            sid = int(input("Enter Student ID: "))
            marks = float(input("Enter New Marks: "))

            cur.execute(
                "UPDATE students SET marks=%s WHERE id=%s",
                (marks, sid)
            )

            con.commit()
            print(cur.rowcount, "record updated")

        elif choice == "4":
            sid = int(input("Enter Student ID: "))

            cur.execute(
                "DELETE FROM students WHERE id=%s",
                (sid,)
            )

            con.commit()
            print(cur.rowcount, "record deleted")

        elif choice == "5":
            print("Exiting application...")
            break

        else:
            print("Invalid choice! Try again.")

except mysql.connector.Error as e:
    print("Database error:", e)

except ValueError:
    print("Please enter valid numeric values.")

finally:
    if "cur" in locals():
        cur.close()

    if "con" in locals() and con.is_connected():
        con.close()