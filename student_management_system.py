# Student Management System using OOP
# Assinment # 06

class Student:
    def __init__(self, student_id, name, age, course):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.course = course

    def update_info(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course

    def display_info(self):
        return f"ID: {self.student_id}, Name: {self.name}, Age: {self.age}, Course: {self.course}"


# Inheritance + method overriding
class GraduateStudent(Student):
    def display_info(self):
        info = super().display_info()
        return f"{info} (Graduate Student)"


class StudentManagementSystem:
    def __init__(self):
        self.students = {}

    def add_student(self):
        student_id = input("Enter Student ID in numbers: ")
        name = input("Enter Name: ")
        age = input("Enter Age: ")
        course = input("Enter Course: ")

        grad = input("Graduate student? (y/n): ")
        if grad.lower() == "y":
            student = GraduateStudent(student_id, name, age, course)
        else:
            student = Student(student_id, name, age, course)

        self.students[student_id] = student
        print("Student added successfully.\n")

    def update_student(self):
        print("\n--- Update Student ---")
        student_id = input("Enter Student ID to update: ").strip()

        student = self.students.get(student_id)
      

        if not student_id:
            print(f" No student found with ID '{student_id}'.")
            return

        print("Current Info:")
        print(" ", student.display_info())
        print("\nLeave a field blank to keep it unchanged.")

        name = input("Enter New Name: ")
        age = input("Enter New Age: ")
        course = input("Enter New Course: ")

        self.students[student_id].update_info(name, age, course)
        print("Student updated successfully.\n")

    def view_students(self):
        if not self.students:
            print("No students found.\n")
            return

        for student in self.students.values():
            print(student.display_info())
        print()

    def run(self):
        while True:
            print("1. Add Student")
            print("2. Update Student")
            print("3. View Students")
            print("4. Exit")

            choice = input("Enter choice: ")

            if choice == "1":
                self.add_student()
            elif choice == "2":
                self.update_student()
            elif choice == "3":
                self.view_students()
            elif choice == "4":
                print("Exiting program.")
                break
            else:
                print("Invalid choice.\n")


system = StudentManagementSystem()
system.run()
