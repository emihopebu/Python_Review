#staticmethod

class Student:
    name="unknown" #class attribute

    def __init__(self):
        self.age=20 #instance attribute

    @staticmethod
    def uni_class():
        return "History"

print(Student.uni_class())
#or
class_student=Student()
print(class_student.uni_class())

