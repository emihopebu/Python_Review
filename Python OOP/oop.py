#OOP

class PlayerCharacter:
    def __init__(self, name, age):
        self.name=name
        self.age=age
    def run(self):
        print("run!")
        return "Done."

player1=PlayerCharacter("Emi",26)
player2=PlayerCharacter("Rachel",50)
player2.attack=50
print(player1.name)
print(player2.name)
print(player1.age)
print(player2.age)
print(player1.run())
print(player1)
print(player2)
print(player2.attack)

