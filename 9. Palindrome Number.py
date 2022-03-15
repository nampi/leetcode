def isPalindrome(x: int) -> bool:
    s = str(x)
    for ind in range(0, len(s) // 2):
        if s[ind] != s[len(s) - 1 - ind]:
            return False

    return True


print(isPalindrome(12321))
