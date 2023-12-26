n = int(input())
answer = 1

for i in range(1, 11):
    answer *= i
    if answer >= n:
        break

print(i)