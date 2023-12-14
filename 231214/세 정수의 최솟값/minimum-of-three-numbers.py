a, b, c = map(int, input().split())

if a >= b and b <= c:
    print(b)
elif b >= a and a <= c:
    print(a)
else:
    print(c)