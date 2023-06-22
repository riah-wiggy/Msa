import Student
#create 2 students

student1 = Student.Student("Jess", "Hanes", "Math", 30 ,3.0, "1234")
student2 = Student.Student("Harry", "Miller", "Ela", 98, 4.0, "23456")

students = []

students.append(student1)
students.append(student2)

for student in students:
    student.print_data()