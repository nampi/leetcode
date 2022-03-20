x, y = map(float, input().split())

eps = 1e-7
n = 1
while x + eps < y:
    x *= 1.7
    n += 1

print(n)
