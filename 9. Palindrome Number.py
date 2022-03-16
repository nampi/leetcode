def is_palindrome(x: int) -> bool:
    s = str(x)
    for ind in range(0, len(s) // 2):
        if s[ind] != s[-1 - ind]:
            return False

    return True


print(is_palindrome(12321))
