x = int(input())
max_elem = x
max_num = 0
while x != 0:
    if x == max_elem:
        max_num += 1
    elif x > max_elem:
        max_elem = x
        max_num = 1
    x = int(input())

print(max_num)