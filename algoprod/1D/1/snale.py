h = int(input())
a = int(input())
b = int(input())
t = (h - a) // (a - b)
if (h - a) % (a - b) != 0:
    t += 1
print(t + 1)
