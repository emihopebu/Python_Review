#scope means what variables do I have access to?

total=100#global scope

if True:
    x=10

def sum_func():
    total_2=200#function scope
    print(total_2)


print(x)
sum_func()
