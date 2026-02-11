from db_connection import get_connection

courses=[
    "Database Management System-I","Design and Analysis of Algorithms-I","Data & Telecommunications","Computer Architecture & Organization","Introduction to Mechatronics","Database Management System-I Lab","Design and Analysis of Algorithms-I Lab","Data & Telecommunications Lab","Application Development Lab"

]
print("Select Courses:")
for i,c in enumerate (courses,1):
    print(f"{i}.{c}")
while True:
    try:
        course_choice=int(input("Enter Choice Number: "))
        if 1<= course_choice <= len(courses):
            break
        else:
            print("Invalid Choice. Try Again!")
    except:
        print("Enter a Number.")
course=courses[course_choice-1]

date = input("Enter Date (DD-MM-YYYY): ")

conn = get_connection()
cursor = conn.cursor()
cursor.execute("SELECT student_id, student_name FROM students")
students = cursor.fetchall()
conn.close()

print("\n--- Students ---")
for i, (sid, name) in enumerate(students, 1):
    print(f"{i}. {sid} - {name}")

present_numbers = input("\nEnter Present Student Numbers (space separated): ").split()
present_numbers = [int(n) for n in present_numbers]

print("\n--- Attendance ---")
print("Course:", course)
print("Date:", date)
print("\nPresent Students:")

for count, n in enumerate(present_numbers, 1):
    sid, name = students[n - 1]
    print(f"{count}. {sid} - {name}")