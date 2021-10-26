#instance method, class method and static method

class Student():
    def __init__(self, first_name, last_name):
        self.first_name=first_name
        self.last_name=last_name
    

rob=Student("Rob","Klein")
print(rob.first_name)

#Another way

class Student():
    def __init__(self, first_name, last_name):
        self.first_name=first_name
        self.last_name=last_name
    

    @classmethod
    def student_name(cls, first_name, last_name):
        return cls(first_name, last_name)
        
    
emily=Student.student_name("Emily", "Fabian")
print(emily.first_name)

#Another way

class Student():
    def __init__(self, first_name, last_name):
        self.first_name=first_name
        self.last_name=last_name
    

    @staticmethod
    def student_name(first_name, last_name):
        return first_name, last_name
        
    
print(Student.student_name("Menna","Hope"))


    
