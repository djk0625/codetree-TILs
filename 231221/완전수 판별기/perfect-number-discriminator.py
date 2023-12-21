n = int(input())
answer = 0

for i in range(1, n):
    if n % i == 0:
        answer += i

if answer == n:
    print("P")
else:
    print("N")