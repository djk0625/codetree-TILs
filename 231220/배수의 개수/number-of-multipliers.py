answer = 0
cnt = 0

for i in range(10):
    a = int(input())

    if a % 3 == 0:
        answer += 1
    
    if a % 5 == 0:
        cnt += 1

print(answer, cnt)