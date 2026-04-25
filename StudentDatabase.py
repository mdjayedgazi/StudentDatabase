# 1. Create the StudentDatabase class
class StudentDatabase:
    student_list = []  # class attribute
    
    @classmethod
    def add_student(cls, student):
        cls.student_list.append(student)
        

# 2. Create the Student class
class Student:
    def __init__(self, student_id, name, department) -> None:
        self.__student_id = student_id
        self.__name = name
        self.__department = department
        self.__is_enrolled = False