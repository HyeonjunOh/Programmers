def solution(lottos, win_nums):
    a = len(set(lottos).intersection(win_nums))
    b = lottos.count(0)
    return [[7-a-b, 6][a+b == 0], [7-a, 6][a == 0]]


print(solution([44, 1, 0, 0, 31, 25], [31, 10, 45, 1, 6, 19]))
print(solution([0, 0, 0, 0, 0, 0], [31, 10, 45, 1, 6, 19]))