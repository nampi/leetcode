a = [int(i) for i in input().split()]

t = 10 * [0]
for x in a:
    t[x] += 1

print(*t[1:])
