def solution(progresses, speeds):
    answer = []
    while progresses:
        cnt = 0
        while progresses[0] < 100:
            progresses = [i+j for i, j in zip(progresses, speeds)]
        while progresses and progresses[0] >= 100:
            progresses.pop(0)
            speeds.pop(0)
            cnt += 1
        answer.append(cnt)
    return answer

print(solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1]))
