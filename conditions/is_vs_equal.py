#is vs equal

print(True==1)#True because both are Truthy
print(""==1)#False because empty string is falsey
print([]==1)#False because empty list is falsey
print(10==10.0)#True because both are truthy
print([]==[])#True because both are falsey
print("1"==1)#checks for the types and returns false
print(0==False)#both are truthly values so True

#is checks if the location in memory where the value is stored the same for both
print(True is 1)
print("" is 1)
print([] is 1)
print(10 is 10.0)
print([]is[])
print("1" is 1)
print(0 is False)

print(True is True)
print("" is "")
print(1 is 1) 
print(10 is 10.0) #they are stored in different locations
print([]is[]) #completely different lists in two different locations
print([1,2,3]is[1,2,3])
print("1" is "1")
print(False is False)



