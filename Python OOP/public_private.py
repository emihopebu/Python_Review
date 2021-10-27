#public and private variables, there is no true private variable, underscore means you shouldn't touch it

#public

class Student:
    schoolName = 'Bratstvo School' # class attribute

    def __init__(self, name, age):
        self.name=name # instance attribute
        self.age=age # instance attribute

std = Student("Milica", 12)
print(std.schoolName)
print(std.name)
print(std.age)

#protected

class Student:
    _schoolName = 'Bratstvo School' # protected class attribute
    
    def __init__(self, name, age):
        self._name=name  # protected instance attribute
        self._age=age # protected instance attribute
std = Student("Marko", 13)
print(std._schoolName)
print(std._name)
print(std._age)
