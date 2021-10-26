#password checker
name=input("What is your name: ")
password=input("What is your password: ")
password_length=len(password)
secret_password=password_length*"*"

print(f"{name}, your password {secret_password} is {password_length} letters long.")
