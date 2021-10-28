#string immutability

name="Sam"

#name[0]="p" doesn't work

last_letters=name[1:2]
print("P"+last_letters)

#string concatenation
x="Hello World"

print(x+" it is beautiful outside!")

letter="z"
print(letter*10)
print(2+3)
print("2"+"3")

print(x.upper())
print(x.split())#creating list of a string-default by empty space

y="Hi this is a string"
print(y.split())
print("Hello, how is it going, is it all good?".split("i"))



