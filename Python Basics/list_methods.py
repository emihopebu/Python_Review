#list methods

basket=[1,2,3,4,5]

print(len(basket))

#adding
basket.append(100)
new_list=basket
print(basket)
print(new_list)

#appends changes the list in place, it doesn't produce the value

basket.insert(4,100)
print(basket)

#insert changes the list in place, it doesn't produce the value
basket.extend([100,101])
print(basket)

#extend changes the list in place, it doesn't produce the value

#removing


basket.pop() #removes the last item
basket.pop()
basket.pop(0) #removes whatever it is at index 0
basket.remove(4) #give it the value you wanna remove
#remove changes the list in place, it doesn't produce the value
#pop returns the value removed
removed=basket.pop(1)
print(removed)
print(basket)
basket.clear()
#clear removes whatever is in the list, returns NONE
print(basket)


