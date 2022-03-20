a, b, c, d = map(int, input().split())
h = abs(a - c)
w = abs(b - d)
x, y = h, w
while y != 0:
    x, y = y, x % y
# Не понимаю почему такая формула (искала объяснение, но не нашла)
print(h + w - x)
