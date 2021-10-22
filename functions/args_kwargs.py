#*args and **kwargs

def super_func(*args):
    print(*args)
    print(args)
    return sum(args)

print(super_func(1,2,3,5,6))

def super_func(*args,**kwargs):
    print(*args)
    print(args)#tuple
    print(kwargs)#dictionary
    total=0
    for items in kwargs.values():
        total+=items
        
    return sum(args)+total

print(super_func(1,2,3,5,6, num1=5, num2=10))



