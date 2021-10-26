#iterables a collection of items : list, tuple, set, dictionary, string - go one by one

users={
    "name":"Golem",
    "age":5006,
    "can_swim":False
    }
for i in users: #prints the keys
    print(i)

for item in users.items(): #prints the k-v pairs
    print(item)#returns tuple

for item in users.items(): #prints the k-v pairs
    key,value=item;
    print(key,value)

for value in users.values(): #prints the values
    print(value)

for key in users.keys(): #prints the keys
    print(key)

for k,v in users.items(): #prints the k-v pairs
    print(k,v)


    
