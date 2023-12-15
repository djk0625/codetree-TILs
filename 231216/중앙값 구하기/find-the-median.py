a, b, c = map(int, input().split())

if (a >= b and c >= a) or (a >= c and b >= a):
    print(a)
elif (b >= a and c >= b) or (a >= b and b >= c):
    print(b)
elif (c >= a and b >= c ) or (c >= b and a >= c):
    print(c)