def plus_one(digits: list[int]) -> list[int]:
    flag = 1
    ind = len(digits) - 1
    a = []
    while ind >= 0:
        cur = digits[ind] + flag
        flag = cur // 10
        c = cur % 10
        a.append(c)
        ind -= 1
    if flag > 0:
        a.append(flag)

    a.reverse()
    return a


def plusOne1(digits: list[int]) -> list[int]:
    flag = 1
    ind = len(digits) - 1

    while ind >= 0:
        cur = digits[ind] + flag
        flag = cur // 10
        digits[ind] = cur % 10
        ind -= 1
    if flag > 0:
        digits.insert(0, flag)

    return digits
