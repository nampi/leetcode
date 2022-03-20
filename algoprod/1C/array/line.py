n = int(input())
a = list(map(int, input().split()))
k = int(input())

left = 0
right = n - 1
while left < right:
    midpoint = (left + right) // 2
    mid = a[midpoint]
    if mid >= k:
        left = midpoint + 1
    elif mid < k:
        right = midpoint - 1

if a[left] >= k:
    print(left + 2)
else:
    print(left + 1)
