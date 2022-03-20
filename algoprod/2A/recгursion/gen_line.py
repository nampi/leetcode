def gen_line(n):
    if n == 1:
        return "A"
    s = gen_line(n - 1)
    return s + chr(ord("A") + n - 1) + s


n = int(input())
print(gen_line(n))
