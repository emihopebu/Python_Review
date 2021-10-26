#dictionary methods 2

user={
    "basket":[1,2,3],
    "greet":"hello",
    "age":20,}

print("basket" in user)
print("size" in user)
print("age" in user.keys())
print("hello" in user.values())
# user.clear()removes in place whatever dictionary has

user2=user.copy()
print(user2)

user.clear()
print(user)
print(user2)
print(user2.pop("age"))
print(user2.popitem()) #  popitem() method removes the last inserted key-value pair from the dictionary and returns it as a tuple

print(user2.update({"age":55}))
print(user2.update({"ages":[11,22,33]}))
print(user2)
