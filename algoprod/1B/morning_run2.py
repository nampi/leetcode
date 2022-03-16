s = input()
if " " in s:
    x, y = map(float, s.split())
else:
    x = float(s)
    y = float(input())

eps = 1e-7
n = 1
total = x
while total + eps < y:
    x = 1.7 * x
    total += x
    n += 1

print(n)