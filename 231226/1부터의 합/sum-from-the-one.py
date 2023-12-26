n = int(input())
answer = 0
sum = 0

for i in range(1, 101):
    answer += 1
    sum += i
    if sum >= n:
        break

print(answer)