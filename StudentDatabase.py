class StudentDatabase:
    student_list = []
    
    @classmethod
    def add_student(cls, student):
        cls.student_list.append(student)
        
    @classmethod
    def get_student_by_id(cls, student_id):
        for student in cls.student_list:
            if student.get_student_id() == student_id:
                return student
        return None
    
    @classmethod
    def view_all_students(cls):
        if not cls.student_list:
            print("No students found.")
            return
        for student in cls.student_list:
            student.view_student_info()
            print('_' * 30)


class Student:
    def __init__(self, student_id, name, department):
        self.__student_id = student_id
        self.__name = name
        self.__department = department
        self.__is_enrolled = False
        
        StudentDatabase.add_student(self)
    
    def get_student_id(self):
        return self.__student_id
    
    def enroll_student(self):
        if self.__is_enrolled:
            print('Error: Student already enrolled.')
        else:
            self.__is_enrolled = True
            print(f'{self.__name} enrolled successfully.')
            
    def drop_student(self):
        if not self.__is_enrolled:
            print('Error: Student is not enrolled.')
        else:
            self.__is_enrolled = False
            print(f'{self.__name} dropped successfully.')
        
    def view_student_info(self):
        status = 'Enrolled' if self.__is_enrolled else 'Not Enrolled'
        print(f'ID: {self.__student_id}')
        print(f'Name: {self.__name}')
        print(f'Department: {self.__department}')
        print(f'Status: {status}')


# Create students
s1 = Student(101, "Jaber", "CSE")
s2 = Student(102, "Jamal", "EEE")
s3 = Student(103, "Jayed", "BBA")


# Menu1
while True:
    print("\n\n--- Student Management System ---")
    print("1. View All Students")
    print("2. Enroll Student")
    print("3. Drop Student")
    print("4. Exit")
    
    choice = input("Enter your choice: ")
    
    if choice == '1':
        StudentDatabase.view_all_students()
        
    elif choice == '2':
        try:
            sid = int(input("Enter student ID to enroll: "))
            student = StudentDatabase.get_student_by_id(sid)

            if student is None:
                print('Error: Invalid student ID.')
            else:
                student.enroll_student()
                
        except ValueError:
            print('Error: Please enter a valid number.')
        
    elif choice == '3':
        try:
            sid = int(input("Enter student ID to drop: "))
            student = StudentDatabase.get_student_by_id(sid)

            if student is None:
                print("Error: Invalid student ID.")
            else:
                student.drop_student()
                print(f'Drop successfully {sid}')
                
        except ValueError:
            print("Error: Please enter a valid number.")

    elif choice == '4':
        print("Exiting program...")
        break
    
    else:
        print("Invalid choice. Try again.")