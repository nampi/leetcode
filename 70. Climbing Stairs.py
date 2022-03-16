def climb_stairs(n: int) -> int:
    a, b = 1, 2
    if n < 3:
        return n
    ind = 3
    while ind <= n:
        a, b = b, a + b
        ind += 1
    return b
