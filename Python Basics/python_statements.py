#Python Statements

st="Sammmy print only the words that start with s in this sentence"

for word in st.split():
    if word[0]=="s" or word[0]=="S":
        print(word)

for num in range(0,11,2):
    print(num)

mylist=[x for x in range(1, 51) if x %3==0]
print(mylist)

st2="Print every word in this sentence that has an even number of letter"

for word in st2.split():
    if len(word)%2==0:
        print(word)

for num in range(1, 101):
    if num%3==0 and num %5==0:
        print("FizzBuzz")
    elif num%3==0:
        print("Fizz")
    elif num%5==0:
        print("Buzz")
    else:
        print(num)

st3="Create a list of the first letters of every word in this string."
a_list=[word[0] for word in st3.split()]
print(a_list)
