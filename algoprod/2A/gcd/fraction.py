a, b = map(int, input().split())
x, y = abs(a), abs(b)
while y != 0:
    x, y = y, x % y
print(a // x, b // x)
