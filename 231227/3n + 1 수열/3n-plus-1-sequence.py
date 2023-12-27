n = int(input())
answer = 0

while True:
    if n == 1:
        break

    answer += 1

    if n % 2 == 0:
        n //= 2
    else:
        n = n * 3 + 1

print(answer)