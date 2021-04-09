def solution(skill, skill_trees):
    cnt = 0
    for i in skill_trees:
        tmp = [i.find(j) for j in skill]
        for j, k in enumerate(tmp):
            if k == -1 and tmp[j+1:j+2] not in [[-1], []]:
                tmp = -1
                break
        else:
            tmp = [j for j in tmp if j != -1]
            if tmp == sorted(tmp):
                cnt += 1
    return cnt


print(solution("CBD", ["BACDE", "CBADF", "AECB", "BDA", "AQE"]))