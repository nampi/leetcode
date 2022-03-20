n = int(input())
s = input()
a = 26 * [0]
for c in s:
    a[ord(c) - ord('A')] += 1

left = ""
right = ""
mid = ""
for i in range(len(a)):
    if a[i] == 0:
        continue
    symbol = chr(ord('A') + i)
    if (mid == "") and (a[i] % 2 == 1):
        mid = symbol
    left += symbol * (a[i] // 2)
    right = symbol * (a[i] // 2) + right

print(left + mid + right)
