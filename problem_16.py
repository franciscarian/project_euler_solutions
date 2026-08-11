def solution():
    num = [int(digit) for digit in str(2**1000)]
    return sum(num)

print(solution())