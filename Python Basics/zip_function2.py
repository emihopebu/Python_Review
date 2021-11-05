#zip function
mylist1=[1,2,3,4,5,6,7,8]
mylist2=["a","b","c","d"]
mylist3=[100,200,300]
for item in zip(mylist1,mylist2,mylist3):
    print(item)

print(list(zip(mylist1,mylist2,mylist3)))

for a, b,c in zip(mylist1,mylist2,mylist3):
    print(b)

print("x" in [1,2,3])
print("x" in ["x","y","z"])
print("a" in "a world")
print("mykey" in {"mykey":345})

d={"mykey":345}
print(345 in d.values())
print(345 in d.keys())

another_list=[10,20,30,40,100]
print(min(another_list))
print(max(another_list))


from random import shuffle

random_list=[1,2,3,4,5,6,7,8,9,10]

shuffle(random_list) #in place function, returns None
print(random_list)

from random import randint

mynum=randint(0, 100)
print(mynum)

result=input("Enter a number here: ")
print(result)
print(type(result))
result=int(result)
print(type(result))
