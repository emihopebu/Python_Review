#walrus operator

a="Helloooooooo"
if ((n:=len(a))>10):
    print(f"Too long {n} elements.")

while((n:=len(a))>1):
    print(n)
    a=a[:-1]#to remove a letter each time
print(a)
