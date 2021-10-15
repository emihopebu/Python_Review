#first gui exercise

picture=[
    [0,0,0,1,0,0,0],
    [0,0,1,1,1,0,0],
    [0,1,1,1,1,1,0],
    [1,1,1,1,1,1,1],
    [0,0,0,1,0,0,0],
    [0,0,0,1,0,0,0],
    ]
for line in picture:
    for num in line:
        if num==0:
            print(" ", end="")
        else:
            print("*", end="")
    print("")
    
