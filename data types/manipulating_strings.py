#Manipulating strings


author="Kafka"
print(author[0])
print(author[1])
print(author[2])
print(author[3])
print(author[4])
print(author[-1])
print(author[-2])
print(author[-3])
print(author[-4])
print(author[-5])

#strings like tuples are immutable
ff="F.Fitzgerald"
ff="F.Scott Fitzgerald"
print(ff)
print("cat"+"in"+"hat")
print("tom"*3)
print("Hello".upper())
print("Goodbye".lower())
print("how are you...".capitalize())

print("Tom {}".format("Sawyer"))
n1=input("Enter a noun: ")
v=input("Enter a verb: ")
adj=input("Enter an adj: ")
n2=input("Enter a noun:  ")
r="The {} {} the {} {}".format(n1,v,adj,n2)
print(r)
print("""I jumped over the puddle. It was 12 feet!""".split("."))

#join method lets you add something in between each character in a string
first_three="abc"
result="$".join(first_three)
print(result)
#you can create string with each word separated by space

words=["The", "fox", "jumped", "over","the","fence","."]
one_string=" ".join(words)
print(one_string)


s=" the "
s.strip()
print(s)




