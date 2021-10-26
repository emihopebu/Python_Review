#scope rules

a=1
def confusion():
    a=5 #local scope
    return a
print(a)#1
print(confusion())#5

#1-start with local

a=1#parent scope
def confusion():
    return a
print(a)
print(confusion())

#2-parent scope

def parent():
    a=10
    def confusion_2():
        return a
    return confusion_2()
print(parent())

#3-global scope
a_2=11
def parent_2():
   
    def confusion_3():
        return a_2
    return confusion_3()
print(parent_2())
#4-built in python function
a_3=22
def parent_3():
   def confusion_4():
        return sum
   return confusion_4()
print(parent_3())


