n = int(input())
answer = []

for i in range(1, n+1):
    if(i % 3 == 0 or i % 10 == 3 or i % 10 == 6 or i % 10 == 9 or i // 10 == 3 or i // 10 == 6 or i // 10 == 9):
        answer.append(0)
    else:
        answer.append(i)

print(*answer)