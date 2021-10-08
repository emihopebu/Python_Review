#built-in functions

greet="helloooo"
print(greet[0:len(greet)])

quote="to be or not to be"
print(quote.upper())
print(quote.capitalize())
print(quote.find("be")) #starts at index 3
print(quote.replace("be","me")) #creating a new string but not assigning

print(quote)

quote_2=quote.replace("be","me")
print(quote_2)
