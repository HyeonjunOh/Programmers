def solution(num):
    if num == 1:
        return 0
    for i in range(500):
        if num % 2: num = num*3+1
        else: num = num//2
        if num == 1:
            return i+1
    return -1

print(solution(626331))