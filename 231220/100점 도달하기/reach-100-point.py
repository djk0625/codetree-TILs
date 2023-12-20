n = int(input())
answer = []

for i in range(n, 101):
    if i >= 90:
        answer.append("A")
    elif i >= 80:
        answer.append("B")
    elif i >= 70:
        answer.append("C")
    elif i >= 60:
        answer.append("D")
    else:
        answer.append("F")

print(*answer)