def romanToInt(self, s: str) -> int:
    dictRomans = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

    ind = 1
    allSum = dictRomans[s[0]]
    cur = s[0]
    while ind < len(s):
        prev = cur
        cur = s[ind]
        if dictRomans[prev] < dictRomans[cur]:
            allSum = allSum - 2 * dictRomans[prev]
        allSum += dictRomans[cur]
        ind += 1

    return allSum
