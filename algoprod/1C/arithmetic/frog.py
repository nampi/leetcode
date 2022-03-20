k, t = map(int, input().split())

# a - define in which directions frog jumps
# a % 2 == 0 -> go to the right
# a % 2 == 1 -> go to the left
a = (t - 1) // k
b = (t - 1) % k + 1

print(abs(k * (a % 2) - b))
