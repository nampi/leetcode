def prime_div(n, k):
    for i in range(k, int(n ** 0.5) + 1):
        if n % i == 0:
            return i
    else:
        return n


n = int(input())
k = 2
is_first = True
while n > 1:
    d = prime_div(n, k)
    while n % d == 0 and n > 1:
        if is_first:
            print(d, end="")
            is_first = False
        else:
            print("*", d, sep="", end="")
        n //= d
    k = d
