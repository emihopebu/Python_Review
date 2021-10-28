#formatting strings

print("This is a string {}".format("INSERTED"))
print("The {2} {1} {0}".format("fox","brown","quick"))
print("The {0} {0} {0}".format("fox","brown","quick"))

print("The {q} {b} {f}".format(f="fox",b="brown",q="quick"))

print("The {f} {f} {f}".format(f="fox",b="brown",q="quick"))

result=100/777
print("The result was {r:1.3f}".format(r=result))

result2=104.12345

print("The result was {r:1.3f}".format(r=result2))


name="Jose"
print("Hello, his name is {}.".format(name))
print(f"Hello, his name is {name}.")

name="Anna"
age="16"
print(f"{name} is {age} years old.")




