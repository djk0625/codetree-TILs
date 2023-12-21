a, b = map(int, input().split())
answer = 1

for i in range(b):
    answer *= a

print(answer)