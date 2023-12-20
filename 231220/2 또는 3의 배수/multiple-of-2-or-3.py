n = int(input())
answer = []

for i in range(1, n+1):
    if i % 2 == 0 or i % 3 == 0:
        answer.append(1)
    else:
        answer.append(0)

print(*answer)