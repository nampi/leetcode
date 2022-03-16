s = input()
max_word = ""
cur_word = ""
for c in s:
    if c != " ":
        cur_word += c
        continue
    if cur_word and len(cur_word) > len(max_word):
        max_word = cur_word
    cur_word = ""

if cur_word and len(cur_word) > len(max_word):
    max_word = cur_word

print(max_word)
print(len(max_word))
