def balancedStringSplit(self, s: str) -> int:
    result = 0
    cursum = 0
    for c in s:
        if c == 'R':
            cursum += 1
        else:
            cursum -= 1
        if cursum == 0:
            result += 1
            cursum = 0
    return result

print(balancedStringSplit("LRRRRLLL"))