n = int(input())
answer = 0

for i in range(1, n+1):
    if i % 2 != 0:
        for j in range(n):
            answer += 1
            print(answer, end=' ')
    else:
        for j in range(n):
            answer += 2
            print(answer, end= ' ')
    print()