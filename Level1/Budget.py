def solution(d, budget):
    d.sort()
    answer = 0
    for i in range(len(d)+1):
        if sum(d[:i]) > budget:
            break
        else:
            answer = i
    return answer

print(solution([2,2,3,3], 10))