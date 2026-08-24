class Student:
    all_students = []
    def __init__(self, name, roll_number, marks, fees):
        self.name = name
        self.roll_number = roll_number
        self.marks = marks
        self.fees = fees
    
    def update_marks(self, new_marks):
        self.marks = new_marks

    def update_fees(self, updated_fees):
        self.fees = updated_fees
    
    def show_details(self):
        print(f"\nStudent Details:")
        print(f"Name: {self.name}")
        print(f"Roll Number: {self.roll_number}")
        print(f"Marks: {self.marks}")
        print(f"Fees: {self.fees}")
    
    @classmethod
    def find_student_by_roll(cls, roll):
        for student in cls.all_students:
            if student.roll_number == roll:
                return student
        return None

    @classmethod
    def add_students(cls):
        name = input("Enter student name: ")
        roll = input("Enter student roll number: ")
        marks = int(input("Enter student marks: "))
        fees = int(input("Enter fees of student: "))
        student = cls(name, roll, marks, fees)
        cls.all_students.append(student)
        print(f"Student {name} added successfully!")

    @classmethod
    def update_student_fees(cls):
        roll = input("Enter student roll number to update fees: ")
        student = cls.find_student_by_roll(roll)
        if student:
            updated_fees = int(input("Enter updated fees: "))
            student.update_fees(updated_fees)
            print(f"fees for {student.name} updated successfully!")
        else:
            print("Student not found.")

    @classmethod
    def update_student_marks(cls):
        roll = input("Enter student roll number to update marks: ")
        student = cls.find_student_by_roll(roll)
        if student:
            new_marks = int(input("Enter new marks: "))
            student.update_marks(new_marks)
            print(f"Marks for {student.name} updated successfully!")
        else:
            print("Student not found.")

    @classmethod
    def show_all_students(cls):
        if not cls.all_students:
            print("No students found.")
            return
        for student in cls.all_students:
            student.show_details()

def menu():
    while True:
        print("\n========CampusMate project=========")
        print("1. Add Student")
        print("2. Update Marks")
        print("3. Update Fees")
        print("4. Show all Student")
        print("5. exit")

        choice = input("Enter your option(1-5): ")
        if choice == '1':
            Student.add_students()
        elif choice == '2':
            Student.update_student_marks()
        elif choice == '3':
            Student.update_student_fees()
        elif choice == '4':
            Student.show_all_students()
        elif choice == '5':
            print("Exiting CampusMate stytem")
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    menu()
        
    