#Thesaurus App
import random


print("\nWelcome to the Thesaurus App.")

#define the thesaurus
thesaurus={
    "hot":["balmy","summery","tropical","boiling","scorching"],
    "cold":["chilly","cool","freezing","frigid","polar"],
    "happy":["content","cheery","merry","jovial","jocular"],
    "sad":["unhappy","downcast","miserable","glum","melancholy"],
    }
print("\nChoose a word from the thesaurus and I will give you a synonym.")
print("\nHere are the words in the thesaurus: ")
for key in thesaurus.keys():
    print("\t-"+key)

#get user input
choice=input("\nWhat word would you like a synonym for: ").lower().strip()

#Provide a random synonym
if choice in thesaurus.keys():
    index=random.randint(0,4)
    print("A synonym for "+choice+ " is " + thesaurus[choice][index]+".")
else:
    print("I am sorry, that word is not currently in the thesaurus.")

#get user input to see the whole thesaurus
choice=input("\nWould you like to see the whole thesaurus (y/n): ").lower().strip()
#show all values in the thesaurus
if choice=="y":
    for key, values in thesaurus.items():
        print("\n"+key.title()+ " synonyms are: ")
        for value in values:
            print("\t-"+ value)
else:
    print("\nI hope you enjoyed the program. Thank you.")



