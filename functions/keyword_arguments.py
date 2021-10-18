def say_hello(name, emoji):
        print(f"Hello {name} {emoji}.")

#positional arguments are arguments that require to be in proper position
say_hello("Emi",":D")

#keyword arguments, not worrying about position

say_hello(emoji=":p",name="Mimi") #this is a bad practice

#default parameters

def say_hello(name="Darth Vader", emoji=":("):
        print(f"Hello {name} {emoji}.")

say_hello()
say_hello("Timmy")


