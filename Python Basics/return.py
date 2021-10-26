#return
def sum(num1,num2):
    return num1+num2

#a function should do one thing really well.
#should return something
# if it returns something then we can it assign to a variable

total=sum(10,5)
print(sum(10, total))

def sum2(num1,num2):
    def another_func(n1,n2):
        return n1+n2
    return another_func(num1, num2) #it doesn't care about the names of the arguments
    print("hello") #it never gets to these lines
    return 5

total2=sum2(10,20)
print(total2)
