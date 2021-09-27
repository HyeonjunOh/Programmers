def solution(sizes):
    answer = 1
    for i in zip(*[[max(j), min(j)] for j in sizes]):
        answer *= max(i)
    return answer



print(solution([[60, 50], [30, 70], [60, 30], [80, 40]]))