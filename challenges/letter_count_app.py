print("Welcome to the Letter Counter App.")

#Get user input
your_name=input("\nWhat is your name: ").title().strip()
print("Hello "+your_name+"!")

print("I will count the number of times that a specific letter occurs in a message.")

#standardize to lower case
message=input("\nPlease enter a message: ").lower()
letter=input("Which letter would you like to count the occurrences of: ").lower()

#get the count and display results
letter_count=message.count(letter)

print("\n"+your_name+ ", your message has "+str(letter_count)+" "+letter+"'s in it.")
