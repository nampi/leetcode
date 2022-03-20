n = int(input())
a = [int(i) for i in input().split()]

idx = 0
max_elem = a[0]
for i, elem in enumerate(a):
    if elem > max_elem:
        max_elem = elem
        idx = i

print(idx + 1)
