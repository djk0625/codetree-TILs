a, b = map(int, input().split())

print(f"{a//b}.", end="")

a %= b
for i in range(20):
    a *= 10
    print(a // b, end="")

    a %= b