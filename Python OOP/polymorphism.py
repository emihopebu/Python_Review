#polymorphism

#polymorphic functions

#len() being used for a string
print(len("hello"))

#len() being used for a list

print(len([10,20,30]))

def add(a,b,c=11):
    return a+b+c

print(add(3,33))
print(add(2,3,4))

#using two different class types in the same way

class Serbia():
    def capital(self):
        print("Belgrade is the capital of Serbia.")
    def language(self):
        print("Serbian is the spoken language of Serbia.")
    def type(self):
        print("Serbia is a developing country.")

class USA():
    def capital(self):
        print("Washington, D.C. is the capital of USA.")
 
    def language(self):
        print("English is the primary language of USA.")
 
    def type(self):
        print("USA is a developed country.")

obj_serb=Serbia()
obj_usa=USA()
for country in (obj_serb, obj_usa):
    country.capital()
    country.language()
    country.type()

# Polymorphism lets us define methods in the child class
#that have the same name as the methods in the parent class.
class Bird:
  def intro(self):
    print("There are many types of birds.")
     
  def flight(self):
    print("Most of the birds can fly but some cannot.")
   
class sparrow(Bird):
  def flight(self):
    print("Sparrows can fly.")
     
class ostrich(Bird):
  def flight(self):
    print("Ostriches cannot fly.")
     
obj_bird = Bird()
obj_spr = sparrow()
obj_ost = ostrich()
 
obj_bird.intro()
obj_bird.flight()
 
obj_spr.intro()
obj_spr.flight()
 
obj_ost.intro()
obj_ost.flight()
    

