a, b = map(int, input().split())
answer = 0
count = 0

for i in range(a, b+1):
    if i % 5 == 0 or i % 7 == 0:
        answer += i
        count += 1

print(answer, round(answer / count, 1))