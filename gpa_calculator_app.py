#GPA Calculator App

print("Welcome to the GPA Calculator App.")

#Get user input
name=input("What is your name: ").title().strip()
grade_num=int(input("How many grades would you like to enter: "))

#get the user's grades
grades=[]
for i in range(grade_num):
    grades.append(int(input("Enter grade: ")))

#sort the grades and print them to the screen
grades.sort(reverse=True)
print("\nGrades Highest to Lowest:")

for grade in grades:
    print("\t"+str(grade))
    
#calculate the average
average=sum(grades)/len(grades)
average=round(average,2)

#Summary results

print("\n"+name+"'s Grade Summary:")
print("\tTotal Number of Grades: "+str(len(grades)))
print("\tHighest grade: "+str(max(grades)))
print("\tLowest grade: "+str(min(grades)))
print("\tAverage: "+str(average))

#Get the user's desired average and calculate what they need to get on the next assignment

desired_avg=float(input("\nWhat is your desired average: "))
grade_req=desired_avg*(len(grades)+1)-sum(grades)
grade_req=round(grade_req,2)

#print a summary

print("\nGood luck "+name+"!")
print("You will need to get a "+str(grade_req) +" on your next assingment to earn a "+str(desired_avg)+" average.")


    















    


