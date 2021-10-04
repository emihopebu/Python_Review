#Database Admin Program

print("Welcome to the Database Admin Program.")

#create a dictionary to hold all username:password key-value pairs

log_on_information={
    "mooman74":"alskes145",
    "meramo1985":"kehns010101",
    "nickyD":"world1star",
    "george2":"booo3oha",
    "admin00":"admin1234",}

#get user input
username=input("Enter your username: ")

#simulate logging on...
#get user password
if username in log_on_information.keys():
    password=input("Enter your password: ")
    if password ==log_on_information[username]:
        print("\nHello, "+username+"! You are logged in!")
        if username=="admin00":
            #show the whole database to the admin account
            print("\nHere is the current user database:")
            for key, value in log_on_information.items():
                print("Username: "+key+"\t\tPassword: "+value)
        else:
            #Allow standard user to change their password
            password_change=input("Would you like to change your password (yes/no): ").lower().strip()
            if password_change=="yes":
                new_password=input("What would you like your new password to be (min 8 chars): ")
                if len(new_password)>=8:
                    log_on_information[username]=new_password
                else:
                    print(new_password +" is not the minimum 8 characters.")
                print("\n"+username+ " your password is " +log_on_information[username]+".")
            else:
               print("Thank you, goodbye.")
    #did not enter the correct password
    else:
        print("Password incorrect.")
#user not in database
else:
    print("User not in database. Goodbye.")
        
        


            
