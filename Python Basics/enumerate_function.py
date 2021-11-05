#enumerate function

mylist=[1,2,3]

for num in range(10):
    print(num)

for num in range(3,10):
    print(num)

for num in range(0,11,2):
    print(num)

print(list(range(1,11,2)))

index_count=0

for letter in "abcde":
    print("At index {} the letter is {} .".format(index_count, letter))
    index_count+=1

#another way

ind_count=0
word="hello"
for l in word:
    print(word[ind_count])
    ind_count+=1

word2="Farewell"
for item in enumerate(word2):
    print(item)


word2="Farewell"
for index,letter in enumerate(word2):
    print(index)
    print(letter)
    print("\n")




