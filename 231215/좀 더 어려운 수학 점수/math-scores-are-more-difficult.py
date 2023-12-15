a, b = map(int, input().split())
c, d = map(int, input().split())

if a > c:
    print("A")
elif a < c:
    print("B")


if a == c:
    if b > d:
        print("A")
    elif b < d:
        print("B")