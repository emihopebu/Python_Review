#dictionary exercise

user={
    "age":22,
    "username":"Maggy",
    "weapons":["scissors","knife"],
    "is_active":True,
    "clan":"visavis",
    }

print(user.keys())
user["weapons"].append("rocks")
print(user)
user.update({"is_banned":False})
print(user)
user["is_banned"]=True
print(user)
user2=user.copy()
user2.update({"age":33})
user2.update({"username":"Rizos"})
print(user2)
