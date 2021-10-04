#coin toss app
import random

print("Welcome to the coin toss app.")
print("\nI will flip a coin a set number of times.")

#get user input

flip_number=int(input("How many times would you like me to flip the coin: "))
choice=input("Would you like to see the result of each flip (y/n): ").lower()

print("\nFlipping!!!\n")

#initialize variables
heads=0
tails=0

#the main loop
for flips in range(flip_number):
    #create the coin object
    coin=random.randint(0,1)
    if coin==1:
        heads=heads+1
        if choice.startswith('y'):
            print("HEADS")
    else:
        tails=tails+1
        if choice.startswith('y'):
            print('TAILS')
    if heads==tails:
        print("At "+str(flips+1)+" flips, the number of heads and tails were equal at "+str(heads)+" each.")

#calculate percentages
        
heads_percentage=round(100*heads/flip_number,2)
tails_percentage=round(100*tails/flip_number,2)

#print the results
print("\nResults of flipping the coin "+str(flip_number)+ "Times: ")
print("\nSide\t\tCount\t\tPercentage")
print("Heads\t\t"+str(heads)+"/"+str(flip_number)+"\t\t"+str(heads_percentage)+"%")
print("Tails\t\t"+str(tails)+"/"+str(flip_number)+"\t\t"+str(tails_percentage)+"%")

