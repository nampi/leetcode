def commonChars(words: list[str]) -> list[str]:
    if len(words) == 0:
        return []

    dictCur = {}
    for c in words[0]:
        if c in dictCur:
            dictCur[c] += 1
        else:
            dictCur[c] = 1

    dictAll = dictCur
    for idx in range(1, len(words)):
        dictAll = dictCur
        dictCur = {}
        for c in words[idx]:
            if c in dictAll:
                dictAll[c] -= 1
                if dictAll[c] == 0:
                    dictAll.pop(c)
                if c in dictCur:
                    dictCur[c] += 1
                else:
                    dictCur[c] = 1

    dictAll = dictCur
    s = []
    for c in dictAll:
        for x in range(0, dictAll[c]):
            s.append(c)
    return s


print(commonChars(["bella", "label", "roller"]))
