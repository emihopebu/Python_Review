#first gui exercise
#clean code
#readability
#predictability
#DRY


picture=[
    [0,0,0,1,0,0,0],
    [0,0,1,1,1,0,0],
    [0,1,1,1,1,1,0],
    [1,1,1,1,1,1,1],
    [0,0,0,1,0,0,0],
    [0,0,0,1,0,0,0],
    ]
fill="*"
empty=" "
for line in picture:
    for num in line:
        if num:
            print(fill, end="")
        else:
            print(empty, end="")
    print("")
    
