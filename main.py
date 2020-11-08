a = int(input())
b = int(input())
c = int(input())
if b <= a >= c:
    print(a)
    if b >= c:
        print(c)
        print(b)
    elif c >= b:
        print(b)
        print(c)
elif a <= b >= c:
    print(b)
    if a >= c:
        print(c)
        print(a)
    elif c >= a:
        print(a)
        print(c)
elif a <= c >= b:
    print(c)
    if b >= a:
        print(a)
        print(b)
    elif a >= b:
        print(b)
        print(a)