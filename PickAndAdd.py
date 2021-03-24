import itertools
def solution(numbers):
    answer = sorted(list(set(map(sum, (itertools.combinations(numbers, 2))))))
    return answer