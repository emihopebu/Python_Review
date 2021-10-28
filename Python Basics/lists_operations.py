#lists

my_list=[1,2,3]

my_list2=["String",100,23,2]

print(len(my_list2))

my_list3=["one","two","three"]

print(my_list3[0])
print(my_list3[1:])

another_list=["four","five"]

print(my_list3+another_list)
new_list=my_list3+another_list
new_list[0]="ONE ALL CAPS"
print(new_list)

new_list.append("six") #adding on the end
new_list.append("seven")

new_list.pop() #removing from the end

print(new_list)

popped_item=new_list.pop()

print(popped_item)

new_list.pop(0)

print(new_list)
char_list=["a","e","x","b","c"]
num_list=[4,1,8,3]

char_list.sort()
print(char_list)
num_list.sort()
print(num_list)

num_list.reverse()
print(num_list)


              
