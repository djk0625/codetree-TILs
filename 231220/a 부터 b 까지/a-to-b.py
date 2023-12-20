a, b = map(int, input().split())
answer = []

for i in range(a, b+1):
    if a > b:
        break
        
    if i % 2 != 0:
        answer.append(a)
        a *= 2
        i = a 
    else:
        answer.append(a)
        a += 3
        i = a
print(*answer)