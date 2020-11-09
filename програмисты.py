x = int(input())
if x == 0:
    print(x, "программистов")
elif x % 10 in [0, 5, 6, 7, 8, 9] or x % 100 in [11, 12, 13, 14]:
    print(x, "программистов")
elif x % 10 in [1]:
    print(x, "программист")
elif x % 10 in [2, 3, 4]:
    print(x, "программиста")