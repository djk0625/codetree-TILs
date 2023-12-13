a, b, c = map(int, input().split())

if min(a,b,c) == a:
    print(1, end=' ')
else:
    print(0, end=' ')

if a == b == c:
    print(1)
else:
    print(0)