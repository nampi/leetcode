s = input()
maxWord = ""
curWord = ""
for c in s:
    if c != " ":
        curWord += c
        continue
    if curWord and len(curWord) > len(maxWord):
        maxWord = curWord
    curWord = ""

if curWord and len(curWord) > len(maxWord):
    maxWord = curWord

print(maxWord)
print(len(maxWord))
