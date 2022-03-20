n = int(input())
a = list(map(int, input().split()))

max_elem = a[0]
for x in a:
    max_elem = max(max_elem, x)

print(max_elem)
