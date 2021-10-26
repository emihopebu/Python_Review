#For loop

teams=["giants","bills","jets","patriots"]
print(teams)
print(type(teams))

print(teams[0].title())
print(teams[1].title())
print(teams[2].title())
print(teams[3].title())


for team in teams:
    print(team.title())
    print("You are going to win the Super Bowl!\n")
print("Go Football!!!")
values=[1,2,3,4,5]
total_sum=0
for value in values:
    total_sum+=value
print(total_sum)

triples=[["a","b","c"],[1,2,3],["do","re","me"]]

for list_value in triples:
    for element in list_value:
        print(element, end=' ')
    print("I just finished one of the inner loops!")
print("Now I am outside both for loops!")


