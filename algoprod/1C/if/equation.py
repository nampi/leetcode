a, b, c = map(int, input().split())

if c < 0:
    print("NO SOLUTION")
elif a == 0 and b >= 0 and b == c * c:
    print("MANY SOLUTIONS")
elif a == 0:
    print("NO SOLUTION")
else:
    tmp = c * c - b
    if tmp % a != 0:
        print("NO SOLUTION")
    else:
        print(tmp // a)
