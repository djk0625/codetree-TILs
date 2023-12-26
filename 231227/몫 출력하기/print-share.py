answer = 0

while True:
    n = int(input())

    if n % 2 != 0:
        continue

    print(n //2)
    answer += 1

    if answer >= 3:
        break