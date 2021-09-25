#Elif Chains

age=int(input("What is your age: "))

if age<18:
    print("You are only " +str(age)+"!")
    print("You cannot gamble!")
elif age<21:
    print("Okay, so you are "+str(age)+"!")
    print("You can play Blackjack but you can't have a drink.")
elif age<100:
    print("Okay good. You are "+str(age)+"!")
    print("You can play Blackjack and you can have a drink.")
else:
    print("What are you doing out at a casino?!?!")

num=40
if num <5:
    print("That's a small number.")
elif num <10:
    print("That is sort of small.")
elif num <15:
    print("That is a medium number.")
elif num <20:
    print("That's sort of medium.")
elif num <25:
    print("That's a large number.")
elif num ==40:
    print("I love that number.")
else:
    print("That number is HUGE!")
    
