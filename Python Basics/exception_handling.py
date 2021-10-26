#exception handling

number=input("Enter a number: ")

try:
    #since we are gonna enter integer and not a float we use int()

    number_int=int(number)

    print(number_int)

except:

    print("Please, type an integer.")
