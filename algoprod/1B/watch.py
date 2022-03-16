h = int(input())
m = int(input())
s = int(input())

seconds_in_day = 12 * 60 * 60
seconds_from_the_beginning = h * 60 * 60 + m * 60 + s
angle = (360.0 * seconds_from_the_beginning) / seconds_in_day
print(angle)
