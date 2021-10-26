#tuples part two

my_tuple=(1,2,3,4,5,2,2,2)
new_tuple=my_tuple[1:2]

print(new_tuple)
x,y,z, *other=(6,7,8,9,10,11,12,13)
print(x)
print(y)
print(other)

print(my_tuple.count(2))
print(my_tuple.index(5))
print(len(my_tuple))

