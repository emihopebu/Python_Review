#short circuiting

is_friend=False
is_user=True

if is_friend and is_user: 
    print("Best friends forever.")
else:
    print("Not friends at all.")

is_animal=True
is_flying=False
if is_animal or is_flying:
    print("It is an animal.")
else:
    print("It is a human.")

