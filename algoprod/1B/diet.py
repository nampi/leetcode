total_x, total_y, total_z = map(float, input().split())
eps = 1e-7
n = int(input())
for _ in range(n):
    x, y, z, q = map(float, input().split())
    total_x -= q * x
    total_y -= q * y
    total_z -= q * z

if ((total_x - eps < 0) and (total_y - eps < 0) and
        (total_z - eps < 0)):
    print("YES")
else:
    print("NO")
