#dictionary

my_dict={
    "key1":"value",
    "key2":"value2",
    }

print(my_dict)

print(my_dict["key1"])

prices_lookup={
    "apple":2.99,
    "oranges":1.99,
    "milk":5.80,
    }

print(prices_lookup["apple"])

d={"k1":123,"k2":[0,1,2],"k3":{"insideKey":100}}
print(d["k2"][2])
print(d["k3"]["insideKey"])

d2={"key1":["a","b","c"]}
print(d2["key1"][2].upper())

d3={"k1":100,"k2":200}
d3["k3"]=300
print(d3)
d3["k1"]="New Value"
print(d3)

#dictionary methods

d4={"key1":11,"key2":22,"key3":33}
print(d4.keys())
print(d4.values())
print(d4.items())
