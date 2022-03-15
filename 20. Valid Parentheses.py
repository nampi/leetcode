PAIRS = {
    '(': ')',
    '[': ']',
    '{': '}',
}


def isvalid(s: str) -> bool:
    stack = []
    for c in s:
        if c in "([{":
            stack.append(c)
            continue
        if not stack:
            return False
        prev = stack.pop()
        if PAIRS[prev] == c:
            continue
        return False
    return not stack


s = '([)]'
flag = isvalid(s)
print(flag)
