#using Python to access the data and to change the data

import os
location=os.path.join("mine.txt")
# r opens the file for reading only
# w opens the file for writing only
# w+ opens the file for reading and writing

creating_file=open("text.txt","w")
creating_file.write("Hi, from Emi.")
creating_file.close()


#second method to create the file
with open("text.txt","w") as f:
          f.write("Hi, from Emi.")

#read the file
with open("text.txt","r") as f:
          print(f.read())

#saving the content in the list

my_list=list()
with open("text.txt","r") as f:
          my_list.append(f.read())
print(my_list)
