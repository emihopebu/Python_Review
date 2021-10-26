#create and write data to csv file
import csv

#opening the file             #writing the file
with open("mine.csv","w",newline="")as f:
          write=csv.writer(f,delimiter=",")
          write.writerow(["one","two","three"])
          write.writerow(["four","five","six"])

#reading from csv file

with open("mine.csv","r")as f:
          r=csv.reader(f,delimiter=",")
          for row in r:
              print(",".join(row))

          
          
          
          
