
def lone_sum(a, b, c):
    
    if a == b and a == c and b == c:
        print (c)
        return c
    elif a == c:
        print (b)
        return b
    elif b == c:
        print (a)
        return a
    elif a >= b:
        print (0)
        return 0
    else:
        print (a + b + c)
        return a+b+c
lone_sum(10, 11, 12)