#list methods exercise

basket=["Banana","Apples","Oranges","Blueberries"]
#removing banana from the list
basket.remove("Banana")
#removing blueberries from the list
basket.pop()
#adding kiwi at the end of the list
basket.append("Kiwi")
#add apples at the beginning of the list
basket.insert(0,"Apples")
#count how many apples in the list
print(basket.count("Apples"))
#empty the basket
basket.clear()
print(basket)
