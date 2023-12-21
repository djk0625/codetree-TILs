n = int(input())
answer = 0

for i in range(n):
    a = int(input())
    answer += a

print(answer, round(answer/n, 1))