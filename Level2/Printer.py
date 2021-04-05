def solution(priorities, location):
    answer = []
    p = [[i, j] for i, j in enumerate(priorities)]
    priorities.sort()
    while True:
        if p[0][1] == priorities[-1]:
            answer.append(p.pop(0))
            priorities.pop()
        else:
            p.append(p.pop(0))
        if answer and answer[-1][0] == location:
            return len(answer)

print(solution([2, 1, 3, 2], 2))