n = int(input())
x, y = map(int, input().split())
while n > 1:
    x, y = y - x, x
    n -= 1
print(x, y)
