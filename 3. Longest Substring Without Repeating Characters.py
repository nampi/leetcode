def lengthOfLongestSubstring(s: str) -> int:
    if len(s) <= 1:
        return len(s)

    i, j = 0, 1
    maxLen = 1
    letters = set(s[i])

    while j < len(s):
        if s[j] in letters:
            maxLen = max(maxLen, len(letters))
            while i < j:
                if s[i] == s[j]:
                    i += 1
                    break
                letters.remove(s[i])
                i += 1
        else:
            letters.add(s[j])
        j += 1

    maxLen = max(maxLen, len(letters))
    return maxLen