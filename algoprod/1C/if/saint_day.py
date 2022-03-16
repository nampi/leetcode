a, b = map(int, input().split())

c = max(a, 1605)
x = (b - c) // 10
if (b - c) % 10 == 0 and a == 1605:
    print(x - 1)
else:
    print(x)
