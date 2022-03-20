n = int(input())
gen_num = 1
cur = 1
for i in range(n):
    print(gen_num)
    cur -= 1
    if cur == 0:
        gen_num += 1
        cur = gen_num
