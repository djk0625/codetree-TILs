cnt= 0
answer = 0

while True:
    n = int(input())
    
    if n >= 30:
        print('{:.2f}'.format(round(answer / cnt, 2)))
        break
    
    cnt += 1
    answer += n