#List slicing
numbers=list(range(1,11))
for num in numbers:
    print(num)
print("\nSlicing")
for num in numbers[5:]:
    print(num)
#reference not a copy
new_numbers=numbers
print(new_numbers)
print(numbers)
numbers.pop()
print(numbers)
print(new_numbers)

numbers=list(range(1,6))
print(numbers)

new_numbers=numbers[:]
numbers.pop()
print(numbers)
print(new_numbers)

names=["John", "Bill", "Marry"]
new_names=names.copy()
print(names)
print(new_names)
new_names[0]=new_names[0].upper()
print(new_names)
print(names)










