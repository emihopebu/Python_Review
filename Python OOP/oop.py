#OOP

class PlayerCharacter:
    #class object attribute is statis
    membership=True
    def __init__(self, name, age):
        if (self.membership): #or PlayerCharcter.membership
            self.name=name #attributes dynamic
            self.age=age
    def run(self, greeting):
        self.greeting=greeting
        print("run!")
        return f"Done, {self.greeting}."
    def shout(self):
       return f"My name is {self.name}." #we cannot do PlayerCharacter name because name is not class object attribute, it is defined in constructor function

player1=PlayerCharacter("Emi",26)
player2=PlayerCharacter("Rachel",50)
player2.attack=50
print(player1.name)
print(player2.name)
print(player1.age)
print(player2.age)
print(player1.run("Goodbye"))
print(player1)
print(player2)
print(player2.attack)

help(PlayerCharacter)#shows the blueprint
help(list)#shows the blueprint
print(player1.membership)
print(player2.membership)
print(player1.shout())

