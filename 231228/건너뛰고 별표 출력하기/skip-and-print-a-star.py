n = int(input())

for j in range(1, n+1):
    print("*" * j)
    print()

for i in range(n, 0, -1):
    print("*" * (i-1))
    print()