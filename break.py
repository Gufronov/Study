x = 1
while x:
    x = int(input())
    if x < 10:
        continue
    elif x >= 100:
        break
    else:
        print(x)
