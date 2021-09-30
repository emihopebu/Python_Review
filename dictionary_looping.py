#Looping through a Dictionary
fav_colors={
    "john":"blue",
    "gabe":"orange",
    "mary":"yellow",
    "mike":"purple",
    "lucas":"yellow",
    "sarah":"green",}



print(fav_colors)
#.items() method will return a list of tuple objects
fav_colors_list=fav_colors.items()
print(fav_colors_list)

for k, v in fav_colors.items():
    print("The key "+k+" has an associated value of "+v+".")

fav_colors_keys=fav_colors.keys()
print(fav_colors_keys)

for name in fav_colors.keys():
    print(name.title()+", thank you for taking the survey.")

if "brooke" not in fav_colors.keys():
    print("Brooke, you should take the survey.")

fav_colors_values=fav_colors.values()
print(fav_colors_values)

print("\nThe colors voted on were: ")

for value in set(fav_colors.values()):
    print(value)











