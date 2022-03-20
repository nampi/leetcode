def gen(i):
    if i == -1:
        print(("".join(a))[::-1])
    else:
        a[i] = "0"
        gen(i - 1)
        a[i] = "1"
        gen(i - 1)


n = int(input())
a = ["0"] * n
gen(n - 1)
