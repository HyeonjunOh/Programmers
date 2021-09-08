def solution(price, money, count):
    result = money - sum(price*(i+1) for i in range(count))
    return -result if result < 0 else 0


print(solution(3, 20, 4))