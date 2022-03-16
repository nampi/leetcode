eps = 1e-8
a = float(input())
b = float(input())
c = float(input())
if abs(a + b - c) < eps:
    print("YES")
else:
    print("NO")
