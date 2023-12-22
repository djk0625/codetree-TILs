a = int(input())
answer = []

for i in range(1, a+1):
    if (i % 2 == 0 and i % 4 !=0) or ((i // 8 % 2 == 0)) or (i % 7 < 4):
        continue
    answer.append(i)

print(*answer)