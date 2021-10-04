#Shipping Accounts Program

#Define our list of users
users=['eramom','footea','davisv','papinukt','allenj']
print("\nWelcome to the shipping accounts program.")

#get user input
username=input("What is your username: ").lower().strip()

#our user is in our list
if username in users:
    #price summary
    print("\nHello "+username+". Welcome back to your account.")
    print("Current shipping prices are as follows:")
    print("\nShipping orders 0 to 100: \t\t$5.10 each")
    print("\nShipping orders 100 to 500: \t\t$5.00 each")
    print("\nShipping orders 500 to 1000: \t\t$4.95 each")
    print("\nShipping over 1000: \t\t\t$4.80 each")

    #Determine price based on how many items are shipped
    quantity=int(input("\nHow many items would you like to ship: "))
    if quantity<100:
        cost=5.10
    elif quantity <500:
        cost=5.00
    elif quantity <1000:
        cost=4.95
    else:
        cost=4.80
    #display final cost
    bill=quantity*cost
    bill=round(bill,2)
    print("To ship "+str(quantity)+ " items it will cost you $"+ str(bill)+" at $" +str(cost)+" per an item.")

    #Place the order if the user desires
    choice=input("\nWould you like to place this order (y/n): ").lower()
    if choice.startswith('y'):
        print("Okay. Shipping your " +str(quantity)+" items.")
    else:
        print("Okay, no order is being placed at this time.")
#Your user is not in the list
else:
    print("Sorry, you do not have an account with us. Goodbye.")
    



        


        
