#dictionary methods

user={
    "basket":[1,2,3],
    "greet":"hello",
    "age":20,
    }
print(user.get("age")) #returns None
print(user.get("age", 55)) #if there is no age

user2=dict(name="JohnJohn")
print(user2)

