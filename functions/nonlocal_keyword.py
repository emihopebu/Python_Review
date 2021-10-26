#non-local keyword

def outer():
    x="local"
    def inner():
        nonlocal x #parent local
        x="nonlocal"
        print("inner:",x)
    inner()
    print("outer:",x)
outer()
