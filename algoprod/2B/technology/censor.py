# 1. Мне нужно использовать: s = s.encode("cp866")?
# 2. Как считать в питоне последнюю строчку ввода, если в ней нет перевода строки?

def is_good_word(w):
    symb = ""
    for c in w:
        if c in symb:
            continue
        else:
            symb += c
    return len(symb) > 3


def is_good_phrase(s):
    marks = ".!?:-,;() "
    word = ""
    all_words = 0
    good_words = 0
    for c in s:
        if c not in marks:
            word += c
        elif word:
            all_words += 1
            good_words += int(is_good_word(word))
            word = ""

    return 2 * good_words > all_words


s = input()
while s:
    if is_good_phrase(s):
        print(s)
    s = input()
