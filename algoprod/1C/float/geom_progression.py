n = int(input())
x = float(input())
s = 1
cur = 1
for i in range(n):
    cur *= x
    s += cur

print(s)