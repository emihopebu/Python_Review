#init

class PlayerCharacter:

    membership = True
    def __init__(self, name="anon", age=0):
        if (age>18):
            self.name=name
            self.age=age
            

player1=PlayerCharacter("Tom",19)
print(player1.age)
print(player1.name)
