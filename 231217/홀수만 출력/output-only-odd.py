a, b = map(int, input().split())
answer = []

for i in range(a, b+1):
    if i % 2 != 0:
        answer.append(i)

print(*answer)