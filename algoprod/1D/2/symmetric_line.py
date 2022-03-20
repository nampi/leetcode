n = int(input())
a = list(map(int, input().split()))
mid = (n - 1) // 2
has_mid_elem = n % 2
i, j = 0, 0
pos = -2
while mid < n - 1:
    if has_mid_elem:
        i, j = mid - 1, mid + 1
    else:
        i, j = mid, mid + 1
    is_correct = True
    while j < n:
        if a[i] != a[j]:
            is_correct = False
            break
        i -= 1
        j += 1
    if not has_mid_elem:
        mid += 1
    has_mid_elem = not has_mid_elem
    if not is_correct:
        continue
    pos = i
    break

if pos == -2:
    pos = n - 2

if pos < 0:
    print(0)
else:
    print(pos + 1)
    for k in range(pos, -1, -1):
        print(a[k], end=" ")
