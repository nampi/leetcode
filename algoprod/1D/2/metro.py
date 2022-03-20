n, a, b = map(int, input().split())
if a < b:
    a, b = b, a
print(min(a - b - 1, (n - a) + (b - 1)))
