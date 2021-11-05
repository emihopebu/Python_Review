#list comprehension

mystring="Hello"
mylist=[]
for letter in mystring:
    mylist.append(letter)

print(mylist)

mylist2=[letter for letter in mystring]
print(mylist2)

mylist3=[x for x in "word"]
print(mylist3)

mylist4=[num**2 for num in range(0,11)]
print(mylist4)

mylist5=[x for x in range(0,11) if x%2==0]
print(mylist5)

celcius=[0,10,20,34.5]

fahrenheit=[((9/5)*temp+32) for temp in celcius]
print(fahrenheit)


#another solution

fahrenheit2=[]
for temp in celcius:
    fahrenheit2.append(((9/5)*temp+32))
print(fahrenheit2)


results=[x if x%2==0 else "Odd" for x in range(0,11)]
print(results)


whatever_list=[]
for x in [2,4,6]:
    for y in [100, 200, 300]:
        whatever_list.append(x*y)
print(whatever_list)

whatever_list2=[x*y for x in [2,4,6] for y in [1,10,100]]
print(whatever_list2)

