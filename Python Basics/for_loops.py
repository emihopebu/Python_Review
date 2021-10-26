#for loops over anything that has collection of items

for item in "Zero to Mastery":
    print(item)

for item in [1,2,3,4]:
    print(item)

for item in {1,2,3,4}:
    print(item)
print("hi.")

for item in (1,2,3,4):
    print(item)
    print(item)
    print(item)
print(item) #by the time loop ends the item is 4
for item in (1,2,3,4):
    for x in ["a","b","c"]:
        print(item, x)
          
