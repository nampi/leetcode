def balancedStringSplit(self, s: str) -> int:  # это был метод класса? раз self остался
    result = 0
    cursum = 0
    for c in s:
        if c == 'R':
            cursum += 1
        else:
            cursum -= 1
        if cursum == 0:  # можно писать if not cursum, но так тоже вполне можно
            result += 1
            cursum = 0  # она уже равна нулю
    return result


print(balancedStringSplit("LRRRRLLL"))
