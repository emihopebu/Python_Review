#set methods
my_set={1,2,3,4,5}
your_set={4,5,6,7,8,9,10}

print(my_set.difference(your_set))
my_set.discard(5)#returns none
print(my_set)

my_set.difference_update(your_set)#returns none
print(my_set)
her_set={22,23,24,33,34,44,45}
his_set={22,33,44}

print(her_set.intersection(his_set))

print(her_set.isdisjoint(his_set))#do they have nothing in common

print(her_set.issubset(his_set))

print(her_set.issuperset(his_set))
print(her_set.union(his_set))


