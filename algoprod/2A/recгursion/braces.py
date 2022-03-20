def braces(s):
    if len(s) < 3:
        return s
    return s[0] + "(" + braces(s[1:-1]) + ")" + s[-1]


s = input()
print(braces(s))
