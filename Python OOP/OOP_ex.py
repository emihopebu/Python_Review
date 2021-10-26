#OOP exercise

class Cat:
    species="mammal"
    def __init__(self, name, age):
        self.name=name
        self.age=age

#instantiating the cat object with 3 cats
peanut=Cat("Peanut",3)
garfield=Cat("Garfield",5)
snickers=Cat("Snickers",1)

#finding the oldest cat

def get_oldest_cat(*args):
    return max(args)

#output

print(f"The oldest cat is {get_oldest_cat(peanut.age,garfield.age,snickers.age)} years old.")
