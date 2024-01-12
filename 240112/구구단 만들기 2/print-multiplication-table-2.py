a, b = map(int, input().split())

for j in range(2, 10, 2):
    for i in range(b, a-1, -1):
        print(f'{i} * {j} = {i * j}', end=" ")

        if i != a:
            print("/", end=" ")
        
    print()