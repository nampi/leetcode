def length_of_longest_substring(s: str) -> int:
    if len(s) <= 1:
        return len(s)

    i, j = 0, 1
    max_len = 1
    letters = set(s[i])

    while j < len(s):
        if s[j] in letters:
            max_len = max(max_len, len(letters))
            while i < j:
                if s[i] == s[j]:
                    i += 1
                    break
                letters.remove(s[i])
                i += 1
        else:
            letters.add(s[j])
        j += 1

    max_len = max(max_len, len(letters))
    return max_len
