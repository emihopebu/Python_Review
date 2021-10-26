#example 1
class MyClass:
    def method(self):
        return 'instance method called', self

    @classmethod
    def classmethod(cls):
        return 'class method called', cls

    @staticmethod
    def staticmethod():
        return 'static method called'


obj=MyClass()
print(obj.method())

#or
print(MyClass.method(obj))#must be called with MyClass instance as first argument(otherwise there is an error)

print(obj.classmethod())#it only has access to MyClass but not to instance object

#or
print(MyClass.classmethod())

print(obj.staticmethod())

#or

print(MyClass.staticmethod())
