def gen(i, k):
    if k == -1:
        return
    if i == -1:
        if k != 0:
            return
        print(("".join(a))[::-1])
    else:
        a[i] = "0"
        gen(i - 1, k)
        a[i] = "1"
        gen(i - 1, k - 1)


n, k = map(int, input().split())
a = ["0"] * n
gen(n - 1, k)
