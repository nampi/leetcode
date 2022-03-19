def roman_to_int(s: str) -> int:
    dict_romans = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

    ind = 1
    all_sum = dict_romans[s[0]]
    cur = s[0]
    while ind < len(s):
        prev = cur
        cur = s[ind]
        if dict_romans[prev] < dict_romans[cur]:
            all_sum = all_sum - 2 * dict_romans[prev]
        all_sum += dict_romans[cur]
        ind += 1

    return all_sum
