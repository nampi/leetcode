a = list(map(int, input().split()))

t = 10 * [0]
for x in a:
    t[x] += 1

print(*t[1:])