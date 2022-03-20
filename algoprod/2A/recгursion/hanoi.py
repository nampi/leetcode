def hanoi(n, start, finish):
    if n > 0:
        cur = 6 - start - finish
        hanoi(n - 1, start, cur)
        print(n, start, finish)
        hanoi(n - 1, cur, finish)


n = int(input())
hanoi(n, 1, 3)
