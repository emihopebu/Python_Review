#while loops
x=0
while x< 5:
    print(f"The current value of x is: {x} ")
    x+=1
else:
    print("X is not less than 5")


mylist=[1,2,3]
for item in mylist:
    #comment
    pass

print("end of my script")

mystring="Sammy"
for letter in mystring:
    if letter=="a":
        continue
    print(letter)

for letter in mystring:
    if letter=="a":
        break
    print(letter)

m=0
while m<5:
    if m==2:
        break
    print(m)
    m+=1
    




