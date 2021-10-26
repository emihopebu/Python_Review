#list slicing
amazon_cart=["notebook",
             "sunglasses",
             "toys",
             "grapes",]
print(amazon_cart)
print(amazon_cart[0:2])

print(amazon_cart[0::2])

#lists are mutable
amazon_cart[0]="laptop"
print(amazon_cart)
print(amazon_cart[0:3]) #with list slicing we create a new list

new_cart=amazon_cart[0:3]
new_cart[0]="gum"
print(new_cart)

#if you want to copy a list :

new_cart=amazon_cart[:]

#this changes the original list

new_cart=amazon_cart

