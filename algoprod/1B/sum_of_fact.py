n = int(input())
total = 1
x = 1.0
for i in range(1, n + 1):
    x = x / i
    total += x

print(total)
