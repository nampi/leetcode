x = int(input())
prev = x
max_k = 0
k = 1
while x != 0:
    x = int(input())
    if x == prev:
        k += 1
    else:
        prev = x
        max_k = max(k, max_k)
        k = 1

print(max_k)
