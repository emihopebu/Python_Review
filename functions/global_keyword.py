#global keyword
a=10
def confusion(b):
    print(b)
    a=90

confusion(300)

total=0
def count():
    global total
    total+=1
    return total
count()
count()
print(count())

#second way

total_2=0
def count_2(total_2):
 
    total_2+=1
    return total_2

print(count_2(count_2(count_2(total_2))))

