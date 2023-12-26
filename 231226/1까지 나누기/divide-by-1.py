n = int(input())
answer = 0

for i in range(1, n+1):
    n //= i
    answer += 1
    if n <= 1:
        break

print(answer)