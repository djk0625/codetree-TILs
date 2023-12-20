n = int(input())

a = 0
b = 0
c = 0

for i in range(1, n+1):
    if i % 10 == 0:
        continue

    if i % 12 == 0:
        c += 1
        
    elif i % 3 == 0:
        if i % 12 == 0:
            c += 1
        b += 1
    
    elif i % 2 == 0:
        if i % 3 == 0:
            if i % 12 == 0:
                c += 1
            b += 1
        elif i % 12 == 0:
            c += 1
        a += 1

print(a, b, c)