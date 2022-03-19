def longest_common_prefix(strs: list[str]) -> str:
    if len(strs) == 0:
        return ""
    if len(strs) == 1:
        return strs[0]

    cur = strs[0]
    for word in strs[1:]:
        pos = 0
        while pos < len(cur) and pos < len(word):
            if cur[pos] != word[pos]:
                break
            pos += 1

        cur = cur[0:pos]
        if pos == 0:
            return ""
    return cur
