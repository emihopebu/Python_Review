#class method example 1

class Fruit:
    name="apples"
    @classmethod
    def fruit_name(cls):
        return f"The name is: {cls.name}"

print(Fruit.fruit_name())


