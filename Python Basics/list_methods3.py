#list methods third part

basket=["a","x","b","c","d","e","d"]
#sort sorts the list in place, it doesn't produce the value
print(basket.sort())
basket.sort()
print(basket)
#sorted is a function and it returns a value, creates new copy of the basket and sorts it
basket_2=["x","w","d","c","f"]
print(sorted(basket_2))
print(basket_2)

basket_3=["r","d","z","e","m"]
new_basket=basket_3.copy()
new_basket.sort()
print(new_basket)

basket.reverse()
print(basket)
