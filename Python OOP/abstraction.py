#abstraction means giving access to only what is necessary
class Grades:
    def __init__(self,grade,name):
        self.grade=grade
        self.name=name
    def writing_grade(self):
        print(f"Hello, {self.name}, your grade is {self.grade}.")

student1=Grades("B","Emi")
student1.writing_grade()

#same as

print((1,2,3,1).count(1)) #we don't need to know how count method was implemented
print(len((1,2,3,3,4)))
