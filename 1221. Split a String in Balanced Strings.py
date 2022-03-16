def balanced_string_split(s: str) -> int:
    result = 0
    cur_sum = 0
    for c in s:
        if c == 'R':
            cur_sum += 1
        else:
            cur_sum -= 1
        if cur_sum == 0:
            result += 1
    return result


print(balanced_string_split("LRRRRLLL"))
