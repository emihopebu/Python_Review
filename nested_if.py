#Nested if statements

our_list=[2]
our_string="a"

if our_list:
    print("This list has something in it.")

if our_string:
    print("This string is not empty.")

teams=["knicks","kings","heat","pacers","celtics","pelicans"]
for team in teams:
    if team.startswith("k"):
        print("The "+team.title()+" could win the NBA Championship this year.")
        if team=="knicks":
            print("I know they will win!")
        else:
            print("They probably won't win though...")
    elif team.startswith("p"):
        print("The "+team.title()+" will probably make the playoffs.")
        if team=="pacers":
            print("They need Reggie Miller back though.")
    else:
        print("The "+team.title()+" stands no chance this year.")
        
