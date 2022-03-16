def common_chars(words: list[str]) -> list[str]:
    if len(words) == 0:
        return []

    dict_cur = {}
    for c in words[0]:
        if c in dict_cur:
            dict_cur[c] += 1
        else:
            dict_cur[c] = 1

    for idx in range(1, len(words)):
        dict_all = dict_cur
        dict_cur = {}
        for c in words[idx]:
            if c in dict_all:
                dict_all[c] -= 1
                if dict_all[c] == 0:
                    dict_all.pop(c)
                if c in dict_cur:
                    dict_cur[c] += 1
                else:
                    dict_cur[c] = 1

    dict_all = dict_cur
    s = []
    for c in dict_all:
        for x in range(0, dict_all[c]):
            s.append(c)
    return s


print(common_chars(["bella", "label", "roller"]))
