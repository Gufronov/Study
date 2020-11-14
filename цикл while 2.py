a = int(input())
b = int(input())
d = 1
while d % b != 0 and d % a != 0:
    d = d+1
print(d)