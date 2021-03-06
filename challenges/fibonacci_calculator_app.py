#Fibonacci Calculator App
print("Welcome to the fibonacci calculator app.")

#get user input
num=int(input("\nHow many digits of the fibonacci sequence would you like to compute: "))

#Compute the values of the fib

fib=[1,1]
for i in range(num-2):
    new_fib=fib[i]+fib[i+1]
    fib.append(new_fib)
#display the fib values

print("\nThe first "+str(num)+" numbers of the fibonacci sequence are: ")
for number in fib:
    print(number)
#Compute the golden ratio

golden=[]
for i in range(len(fib)-1):
    ratio=fib[i+1]/fib[i]
    golden.append(ratio)

#display the golden values

print("\nThe corresponding Golden ratio values are: ")
for ratio in golden:
    print(ratio)

print("\nThe ratio of consecutive fibonacci terms approaches Phi;1.618...")
