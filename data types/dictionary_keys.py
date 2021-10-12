#dictionary keys
dictionary={
    123:[1,2,3],
    True:"hello",
    "is_magic":True,
    "is_magic":False}
print(dictionary[123])
print(dictionary[True])
print(dictionary["is_magic"])
#a key needs to be immutable so a list as a key doesn't work
#a key has to be unique
