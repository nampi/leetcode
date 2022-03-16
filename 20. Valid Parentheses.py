PAIRS = {
    '{': '}',
    '[': ']',
    '(': ')'
}


def is_valid(s: str) -> bool:
    stack = []
    for c in s:
        if c in PAIRS:
            stack.append(c)
            continue
        if not stack:
            return False
        prev = stack.pop()
        if PAIRS[prev] != c:
            return False

    return not stack


global_s = '([)]'
flag = is_valid(global_s)
print(flag)
