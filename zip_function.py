#The zip function
names=["jack","john","mark","bill"]
numbers=[20, 44, 3, 14]

for i in range(len(names)):
    print(names[i].title()+": "+str(numbers[i]))
for name,number in zip(names, numbers):
    print(name.title()+": "+str(number))
