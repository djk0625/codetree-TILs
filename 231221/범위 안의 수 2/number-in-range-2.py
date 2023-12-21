answer = 0
count = 0

for i in range(10):
    n = int(input())

    if n >= 0 and n <= 200:
        answer += n
        count += 1

print(answer, round(answer / count, 1))