def gen(i):
    if i == -1:
        print(("".join(a))[::-1])
    else:
        for k in range(n):
            if not was[k]:
                was[k] = True
                a[i] = str(k + 1)
                gen(i - 1)
                was[k] = False


n = int(input())
a = ["0"] * n
was = [False] * n
gen(n - 1)
